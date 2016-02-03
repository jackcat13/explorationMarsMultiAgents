from Content import Content

#Empty class which extends Content class. This class describes an empty content in the environment.
class Empty(Content):

    def __init__(self):
        Content.__init__(self, 'empty')