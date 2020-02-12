#Larissa Pokam

#Project1: Create a Blockchain that represent the chain of custody

import hashlib
import json
from time import time
from Block import Block


class Blockchain():

    #Blockchain Constructor
    def __init__(self):
        self.blocks = [self.first()] #Create a list containing the initial element

    #Create the initial block
    def first(self):
        return Block(0, 0000, time(), "None", "None", "INITIAL", 14, "Initial BLock")

    #Add a new block to the chain
    def add(self, case, item):
       self.blocks.append(Block(len(self.blocks), self.blocks[len(self.blocks)-1].hash, time(),
                          case, item, "Checkin", 14, "First"))

    #Get the number of block in the chain
    def size(self):
       return len(self.blocks)


