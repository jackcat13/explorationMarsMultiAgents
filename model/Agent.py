from Content import Content
from Empty import Empty

#Agent class which extends Content class. This class describes an Agent in the environment
class Agent(Content):

    def __init__(self, name, posX, posY):
        Content.__init__(self, name)
        self.next
        self.posX = posX
        self.posY = posY

    def next(self):
        return self.next

    def setNext(self, next):
        self.next = next

    def terminate(self):
        del self

    def move(self, directionX, directionY, environment):
        self.moveX(directionX, environment)

    def moveX(self, directionX, environment):
        #If explorator goes on the left
        if directionX == 0:
            self.moveXLeft(directionX, environment)
        #else if explorator goes on the right
        else:
            self.moveXRight(directionX, environment)

    def moveXLeft(self, directionX, environment):
        #If explorator is not on the left border and if the box on the left in the environment is empty
        if self.posX > 0 & isinstance(environment[self.posX-1, self.posY], Empty):
            #Then move to the left
            environment[self.posX, self.posY] = Empty()
            environment[self.posX-1, self.posY] = self

    def moveXRight(self, directionX, environment):
        #If explorator is not on the right border and if the box on the right in the environment is empty
        if self.posX < environment.length & isinstance(environment[self.posX+1, self.posY], Empty):
            environment[self.posX, self.posY] = Empty()
            environment[self.posX+1, self.posY] = self