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
        self.name = set_name()
        self.listeners = set_listensers()
        self.url = set_url()
        self.image = set_image()

    def set_name():
        return self.data['name']

    def set_listensers():
        return self.data['listeners']

    def set_url():
        return self.data['url']

    def set_image():
        dict = {}
        for i range(len(data['image'])):
            dict[data['image'][i]['size']] = data['image'][i]['#text']
        return dict
