#Larissa Pokam

#Project1: Create a Blockchain that represent the chain of custody

import hashlib
import json
from time import time


#This class defines the attributes of a single block in the blockchain

class Block():

    # init method or constructor of the block class

    def __init__(self, blockNumber, prevHash, timestamp, caseID, evidenceID, state, dataLength, data):
        self.blockNumber = blockNumber
        self.timestamp = timestamp
        self.state = state
        self.caseID = caseID
        self.data = data
        self.dataLength = dataLength
        self.prevHash = prevHash
        self.evidenceID = evidenceID
        self.hash = self.hashing()



    # This function defines the hash of the previous block x-1, H(Block[x-1]).

    def hashing(self):
        key = hashlib.sha256()
        key.update(str(self.blockNumber).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.state).encode('utf-8'))
        key.update(str(self.caseID).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.prevHash).encode('utf-8'))
        key.update(str(self.evidenceID).encode('utf-8'))
        return key.hexdigest() #the hash of the current block