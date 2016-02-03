from Agent import Agent

#Explorator class which extends Agent class. This class describes how an explorator agent is working
class Explorator(Agent):

    def __init__(self):
        Agent.__init__(self, 'explorator')