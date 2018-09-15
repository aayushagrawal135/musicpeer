# not called from routes.py as of now because unable to pass object 'Track' between
# .html and .py | Resolve that first

from myApp import root_url, API_KEY
import requests
from myApp.Track import Track

class TrackList():
    def __init__(self, artist):
        self.data = self.set_results(artist)
        self.track_result_list = self.set_track_result_list()

    def set_results(self, artist):
        url = root_url + "?method=artist.gettoptracks&artist="+ artist + "&api_key=" + API_KEY + "&format=json"
        PARAMS = {'artist':artist, 'limit':10}

        response = requests.get(url = url, params = PARAMS)
        data = response.json()
        return data['toptracks']['track']

    def set_track_result_list(self):
        res = []
        for i in range(len(self.data)):
            value = Track(self.data[i])
            res.append(value)
        return res

    def get_results(self):
        return self.track_result_list
