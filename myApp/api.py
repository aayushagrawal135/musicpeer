import requests
# ?method=artist.search&artist=cher&api_key=YOUR_API_KEY&format=json

class QueryResponse():
    root_url = "http://ws.audioscrobbler.com/2.0/"
    API_KEY = "a0b8a0a745497e69b39e4815af5e923d"
    data = None

    def __init__(self, artist):
        url = str(self.root_url) + "?method=artist.search&artist=" + artist + "&api_key=" + str(self.API_KEY) + "&format=json"
        PARAMS = {'artist':artist, 'limit':10}

        response = requests.get(url = url, params = PARAMS)
        # extracting data in json format
        #print(response.text)
        self.data = response.json()
        #ontour, mbid, tags, image, streamable, similar, stats, url, name, bio
        # these are the keys in data['artist'] dictionary

    # return a dictionary which contains <similarArtists name>, <link to their image>
    def get_results(self):
        data = self.data['results']['artistmatches']['artist'][1]
        return data

res = QueryResponse("Sean")
print(res.get_results())
