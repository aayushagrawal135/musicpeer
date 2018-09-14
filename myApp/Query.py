# break down each object requested from resultpage, make the object, fill it with members,
# give the object (individual object) to result quesry

# image, streamable, name, mbid, listeners, url
class ResultQuery():
    image = None
    name = None
    listeners = None
    url = None
    data = None

    def __init__(self, inp):
        self.data = inp
        
        self.name = self.set_name()
        self.listeners = self.set_listensers()
        self.url = self.set_url()
        self.image = self.set_image()

    def set_name(self):
        return self.data['name']

    def set_listensers(self):
        return self.data['listeners']

    def set_url(self):
        return self.data['url']

    def set_image(self):
        dict = {}
        for i in range(len(self.data['image'])):
            dict[self.data['image'][i]['size']] = self.data['image'][i]['#text']
        return dict
