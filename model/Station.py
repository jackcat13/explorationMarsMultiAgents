from Agent import Agent

#Station class which extends Agent. This class describes the spatial station which has landed on Mars
class Station(Agent):

    def __init__(self):
        Agent.__init__(self, 'station')