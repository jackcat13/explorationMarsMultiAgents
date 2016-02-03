from Content import Content

#Agent class which extends Content class. This class describes an Agent in the environment
class Agent(Content):

    def __init__(self, name):
        Content.__init__(self, name)
        self.next

    def next(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def terminate(self):
        del self