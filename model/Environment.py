from Empty import Empty

#Environment class. This class describes the simulation environment in which mars exploration is simulated.
class Environment:

    def __init__(self, name, height, length):
        self.name = name
        self.height = height
        self.length = length
        #Init all boxes with an empty content in contentTable
        self.contentTable = [[Empty]*height]*length
        for i in range(height):
            for j in range(length):
                self.contentTable[i][j] = Empty('0')

    '''
    Getters
    '''
    def getContentTable(self):
        return self.contentTable

    def getWeight(self):
        return self.height

    def getLength(self):
        return self.length

    def getName(self):
        return self.name