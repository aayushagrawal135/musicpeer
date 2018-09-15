# not called from routes.py as of now because unable to pass object 'Track' between
# .html and .py | Resolve that first

class Track():

    name = None
    stats = None
    url = None
    artist = None
    image = None

    def __init__(self, inp):
        self.data = inp
        self.name = self.set_name()
        self.stats = self.set_stats()
        self.url = self.set_url()
        self.artist = self.set_artist()
        self.image = self.set_image()

    # return string
    def set_name(self):
        return self.data['name']

    # return dictionary with keys called 'listeners' and 'playcount'
    def set_stats(self):
        dict = {}
        dict['listeners'] = self.data['listeners']
        dict['playcount'] = self.data['playcount']
        return dict

    # return string
    def set_url(self):
        return self.data['url']

    # return a dictionary with keys : 'url' (url of artist), 'name'
    def set_artist(self):
        return self.data['artist']

    # return a dictionary with keys: 'small', 'medium', 'large', 'extralarge'
    def set_image(self):
        dict = {}
        for i in range(len(self.data['image'])):
            dict[self.data['image'][i]['size']] = self.data['image'][i]['#text']
        return dict
