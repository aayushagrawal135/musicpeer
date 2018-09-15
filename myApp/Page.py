# this will be called by outside world. Everyone wants page results
# inside it will call to result query to make an object and bring here
# finally this file will make a neat list of the received from result query
import requests

from myApp import API_KEY, root_url
from myApp.Query import ResultQuery

class ResultPage():
    
    def __init__(self, query):
        self.data = self.set_results(query)
        self.result_list = self.set_list()

    def set_results(self, artist):
        url = root_url + "?method=artist.search&artist=" + artist + "&api_key=" + API_KEY + "&format=json"
        PARAMS = {'artist':artist, 'limit':30}

        response = requests.get(url = url, params = PARAMS)
        temp = response.json()
        return temp['results']['artistmatches']['artist']

# return a list of objects where each query-result is present in individual queries
    def set_list(self):
        res = []
        for i in range(len(self.data)):
            value = ResultQuery(self.data[i])
            res.append(value)

        return res

    def get_results(self):
        return self.result_list
