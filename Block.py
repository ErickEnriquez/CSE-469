#Larissa Pokam
#Erick Enriquez

#Group Project: Create a Blockchain that represent the chain of custody

import hashlib
from uuid import UUID, uuid4
import binascii

#This class defines the attributes of a single block in the blockchain

class Block():

    # init method or constructor of the block class

    def __init__(self, prevHash, timestamp, caseID, evidenceID, state, dataLength, data='0'):#default value for data
        self.timestamp = timestamp
        self.state = state
        self.caseID = caseID
        self.data = data
        self.dataLength = int(dataLength)
        self.prevHash = prevHash
        self.evidenceID = int(evidenceID)
        self.hash = self.hashing()


    # This function defines the hash of the current block i H(Block[i]).

    def hashing(self):
        key = hashlib.sha1()        #hash using the SHA-1 algorithm
        key.update(str(self.timestamp).encode('utf-8'))
        key.update(str(self.state).encode('utf-8'))
        key.update(str(self.caseID).encode('utf-8'))
        key.update(str(self.data).encode('utf-8'))
        key.update(str(self.prevHash).encode('utf-8'))
        key.update(str(self.evidenceID).encode('utf-8'))
        print(binascii.hexlify(key.digest()))
        return key.digest() #the hash of the current block
    



#creates the inital block
def create_initial_block():
    initial_block = Block(
        0,  # 20 bytes : prev hash
        0,  # 08 bytes : timestamp
        0,  # 16 bytes : caseId
        UUID(int=0),  # 04 bytes : evidenceId
        b"INITIAL\0\0\0\0", # 11 bytes : state
        14, # 04 bytes : data_length
        b"Initial block\0" # varies bytes : data
        )
    return initial_block

#untility function to print the block
def printBlock(Block):
    print('\n')
    print(
    Block.prevHash, 
    Block.timestamp,
    Block.caseID,
    Block.evidenceID,
    Block.state,
    Block.dataLength,
    Block.data )
    print('\n\n')

  