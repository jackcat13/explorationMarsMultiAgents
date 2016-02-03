#Content class. This class describes a box in the environment.
class Content:

    def __init__(self, name):
        self.name = name

    '''
    Getters
    '''
    def getName(self):
        return self.name