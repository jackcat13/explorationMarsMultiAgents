from Empty import Empty
from Explorator import Explorator
from Station import Station
from Tkinter import *

#Environment class. This class describes the simulation environment in which mars exploration is simulated.
class Environment:

    def __init__(self, name, height, length):
        self.name = name
        self.height = height
        self.length = length
        #Init all boxes with an empty content in contentTable
        self.contentTable = []
        for i in range(height):
            self.contentTable.append([])
            for j in range(length):
                self.contentTable[i].append(Empty())
        self.contentTable[1][1] = Station()
        self.contentTable[3][1] = Explorator()
        self.UI = Tk()
        self.showEnvironment()

    def showEnvironment(self):
        img = []
        cptImg = 0
        for i in range(self.height):
            for j in range(self.length):
                img.append(PhotoImage(file=self.contentTable[i][j].getPhoto()))
                Label(self.UI, image=img[cptImg], height=20, width=20).grid(row=i, column=j)
                cptImg = cptImg + 1
            print ''
        self.UI.mainloop()

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