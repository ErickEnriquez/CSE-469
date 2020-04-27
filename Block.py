#Larissa Pokam
#Erick Enriquez
#Zayne Bamond

#Group Project: Create a Blockchain that represent the chain of custody

import hashlib
from uuid import UUID, uuid4
import binascii
from datetime import datetime

#This class defines the attributes of a single block in the blockchain

class Block():

    # init method or constructor of the block class

    def __init__(self ,prevHash, timestamp, caseID, evidenceID, state, dataLength, data=b''):#default value for data
        self.prevHash = prevHash
        self.timestamp = timestamp
        self.caseID = caseID
        self.state = state
        self.evidenceID = int(evidenceID)
        self.dataLength = int(dataLength)
        self.data = data  #Me
       

    
# This function defines the hash of the current block i H(Block[i]).

def hashing(Block):
    key = hashlib.sha1()        #hash using the SHA-1 algorithm
    key.update(str(Block.prevHash).encode('utf-8'))
    key.update(str(Block.timestamp).encode('utf-8'))
    key.update(str(Block.caseID).encode('utf-8'))
    key.update(str(Block.evidenceID).encode('utf-8'))
    key.update(str(Block.dataLength).encode('utf-8'))
    key.update(str(Block.data).encode('utf-8'))
    #print(key.digest_size)
    return str(key.hexdigest()) #the hash of the current block    



#creates the inital block
def create_initial_block():
    initial_block = Block(
        str(0),  # 20 bytes : prev hash
        datetime.fromtimestamp(0),  # 08 bytes : timestamp
        UUID(int=0),  # 16 bytes : caseId
        0,  # 04 bytes : evidenceId
        b"INITIAL\0\0\0\0", # 11 bytes : state
        14, # 04 bytes : data_length
        b'',
        )
    initial_block.data = b"Initial block\0" # varies bytes : data
    return initial_block

#untility function to print the block
def printBlock(Block):
    print('\n')
    print(
    Block.prevHash, '\n' , 
    Block.timestamp, '\n' ,
    Block.caseID, '\n' ,
    Block.evidenceID, '\n' ,
    Block.state, '\n' ,
    Block.dataLength, '\n' ,
    Block.data )
    print('\n\n')

  