from model import Environment
from functions import *

print 'Simulation begins'
print 'Height: '
height = input()
print 'Length: '
length = input()

environment = Environment('MarsExploration', height, length)
showEnvironment(environment)
