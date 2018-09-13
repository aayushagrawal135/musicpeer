<<<<<<< HEAD
# once you click on a particular artist, you can get all about him

=======
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
from myApp import API_KEY, root_url

#ontour, mbid, tags, image, streamable, similar, stats, url, name, bio
class Artist():
    data = None
    ontour = None
    tags = None
    image = None
    similar = None
    stats = None
    name = None
    bio = None

    def __init__(self, atist_name):
<<<<<<< HEAD
        self.data = set_artist(artist_name)

        self.name = set_name()
        self.similar = set_similar_artist()
        self.bio = set_bio()
        self.image = set_image()
        self.ontour = set_ontour()
        self.tags = set_tags()

    def set_artist(self, artist):
=======
        self.data = get_artist(artist_name)

        self.name = get_name()
        self.similar = get_similar_artist()
        self.bio = get_bio()
        self.image = get_image()
        self.ontour = get_ontour()
        self.tags = get_tags()

    def get_artist(self, artist):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        url = root_url + "?method=artist.getinfo&api_key=" + API_KEY + "&format=json"
        PARAMS = {'artist':artist}

        response = requests.get(url = url, params = PARAMS)
        return response.json()

<<<<<<< HEAD
    def set_name(self):
=======
    def get_name(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'name' in self.data['artist']:
            return self.data['artist']['name']
        else:
            return None

    # returns a list of names of similar artist
<<<<<<< HEAD
    def set_similar_artist(self):
=======
    def get_similar_artist(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'similar' in self.data['artist'] and 'artist' in self.data['artist']['similar']:
            result = self.data['artist']['similar']['artist']
            similarArtist = []
            for x in result:
                similarArtist.append(x['name'])
            return similarArtist
        else:
            return None

    # returns a string with content about artist <a></a> tags at the end referring a link to read more
<<<<<<< HEAD
    def set_bio(self):
=======
    def get_bio(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'bio' in self.data['artist'] and 'summary' in self.data['artist']['bio']:
            about = self.data['artist']['bio']['summary']
            about = temp.replace("\n", " ")
            about = temp.replace("\t", " ")
            return about
        else:
            return None

    # return a dicionary type with key as size of image, value as link to image
    # permissible key values are: 'large', 'mega', 'small', 'extralarge', 'medium'
<<<<<<< HEAD
    def set_image(self):
=======
    def get_image(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
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
<<<<<<< HEAD
    def set_ontour(self):
=======
    def get_ontour(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'ontour' in self.data['artist']:
            return self.data['artist']['ontour']
        else:
            return None

    # return a dictionary type with key as name of the tag and a link from that tag
    # it works like a hashtag
<<<<<<< HEAD
    def set_tags(self):
=======
    def get_tags(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'tags' in self.data['artist'] and 'tag' in self.data['artist']['tags']:
            data = self.data['artist']['tags']['tag']
            tags = {}
            for i in range(len(data)):
                tags[data[i]['name']] = data[i]['url']
            return tags
        else:
            return None

    #  returrns a dictionary with permissible keys as 'listeners' and 'playcount'
<<<<<<< HEAD
    def set_stats(self):
=======
    def get_stats(self):
>>>>>>> 756dd24972f654d00e303e606735f0dfa94e513f
        if 'artist' in self.data and 'stats' in self.data['artist']:
            return self.data['artist']['stats']
        else:
            return None
