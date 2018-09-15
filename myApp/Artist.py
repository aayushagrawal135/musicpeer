# once you click on a particular artist, you can get all about him
import requests
from myApp import API_KEY, root_url

#ontour, mbid, tags, image, streamable, similar, stats, url, name, bio
class Artist():

    def __init__(self, artist_name):
        self.data = self.set_artist(artist_name)
        self.stats = self.set_stats()
        self.name = self.set_name()
        self.similar = self.set_similar_artist()
        self.bio = self.set_bio()
        self.image = self.set_image()
        self.ontour = self.set_ontour()
        self.tags = self.set_tags()

    # make URL, pass parameters, get response, get it in JSON
    def set_artist(self, artist):
        url = root_url + "?method=artist.getinfo&api_key=" + API_KEY + "&format=json"
        PARAMS = {'artist':artist}

        response = requests.get(url = url, params = PARAMS)
        return response.json()

    # All below methods take out some of the attributes from JSON output. Return
    # format metioned above all functions

    def set_name(self):
        if 'artist' in self.data and 'name' in self.data['artist']:
            return self.data['artist']['name']
        else:
            return None

    # returns a list of names of similar artist
    def set_similar_artist(self):
        if 'artist' in self.data and 'similar' in self.data['artist'] and 'artist' in self.data['artist']['similar']:
            result = self.data['artist']['similar']['artist']
            similarArtist = []
            for x in result:
                similarArtist.append(x['name'])
            return similarArtist
        else:
            return None

    # returns a string with content about artist <a></a> tags at the end referring a link to read more
    def set_bio(self):
        if 'artist' in self.data and 'bio' in self.data['artist'] and 'summary' in self.data['artist']['bio']:
            str = self.data['artist']['bio']['summary'].split('<a')
            about = str[0]
            extra = '<a '+str[1]
            extra = extra.split('href=')[1]
            extra = extra.split(">")[0]
            about = about.replace("\n", " ")
            about = about.replace("\t", " ")
            return about, extra[1:-2]
        else:
            return None

    # return a dicionary type with key as size of image, value as link to image
    # permissible key values are: 'large', 'mega', 'small', 'extralarge', 'medium'
    def set_image(self):
        if 'artist' in self.data and 'image' in self.data['artist']:
            data = self.data['artist']['image']
            img = {}
            for i in range(len(data)):
                if data[i]['size'] != '':
                    img[data[i]['size']] = data[i]['#text']
            return img
        else:
            return None

    # return either 0 or 1, that either artist is on tour or he/she is not on tour
    def set_ontour(self):
        if 'artist' in self.data and 'ontour' in self.data['artist']:
            return self.data['artist']['ontour']
        else:
            return None

    # return a dictionary type with key as name of the tag and a link from that tag
    # it works like a hashtag
    def set_tags(self):
        if 'artist' in self.data and 'tags' in self.data['artist'] and 'tag' in self.data['artist']['tags']:
            data = self.data['artist']['tags']['tag']
            tags = {}
            for i in range(len(data)):
                tags[data[i]['name']] = data[i]['url']
            return tags
        else:
            return None

    #  returrns a dictionary with permissible keys as 'listeners' and 'playcount'
    def set_stats(self):
        if 'artist' in self.data and 'stats' in self.data['artist']:
            return self.data['artist']['stats']
        else:
            return None
