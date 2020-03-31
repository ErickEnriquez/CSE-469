#Larissa Pokam
#Erick Enriquez

#Group Project: Create a Blockchain that represent the chain of custody

import hashlib

#This class defines the attributes of a single block in the blockchain

class Block():

    # init method or constructor of the block class

    def __init__(self, blockNumber, prevHash, timestamp, caseID, evidenceID, state, dataLength, data, parent):
        self.blockNumber = blockNumber
        self.timestamp = timestamp
        self.state = state
        self.caseID = caseID
        self.data = data
        self.dataLength = dataLength
        self.prevHash = prevHash
        self.evidenceID = evidenceID
        self.parent = parent
        self.hash = self.hashing()


    # This function defines the hash of the current block i H(Block[i]).

    def hashing(self):
        key = hashlib.sha1()        #hash using the SHA-1 algorithm
        key.update(str(self.blockNumber).encode('utf-8'))
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.state).encode('utf-8'))
        key.update(str(self.caseID).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.prevHash).encode('utf-8'))
        key.update(str(self.evidenceID).encode('utf-8'))
        key.update(str(self.parent).encode('utf-8'))
        return key.hexdigest() #the hash of the current block