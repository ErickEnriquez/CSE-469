# Larissa Pokam
# Erick Enriquez

# Project1: Create a Blockchain that represent the chain of custody

import datetime
import uuid
import struct
from datetime import datetime, timedelta, timezone
import sys
import os
from uuid import UUID

from Block import Block
from BlockPack import unpack, pack_block
import binascii

from Block import hashing

import Block
#Block.Block()


# blocks = Block.Block()

class Blockchain():

    # Blockchain Constructor
    def __init__(self):
        self.blocks = []  # create empty list to hold items


    # Add a new block to the chain and make sure there is no item duplicate
    def add(self, case, item):
        exist = 0
        for j in range(0, len(self.blocks)):
            if str(self.blocks[j].evidenceID) == item:
                exist = 1
        if exist == 1:
            sys.exit("This item already exists in the blockchain")
        else:
            if len(self.blocks) == 1:
                self.blocks.append(Block.Block(
                   str(0),
                   datetime.now(),
                   UUID(case),
                   item,
                   STATE['in'],
                   0 
                ))
            else:
                self.blocks.append(Block.Block(
                                    str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                                    datetime.now(),                             #timestamp
                                    UUID(case),                                   #caseID
                                    item,                                   #evidence id
                                    STATE['in'],                            #state
                                    0                                      #datalength
                                     ))
            print('Case: ', self.blocks[len(self.blocks) - 1].caseID)
            print('item ID: ', self.blocks[len(self.blocks) - 1].evidenceID)
            print('Status: ', self.blocks[len(self.blocks) - 1].state.decode('utf-8'))
            print('Time of action: ', self.blocks[len(self.blocks) - 1].timestamp.isoformat())
            print('previous hash: ' , self.blocks[len(self.blocks)-1].prevHash , " TYPE: ", type(self.blocks[len(self.blocks)-1].prevHash) ,len(self.blocks[len(self.blocks)-1].prevHash))

    # Get the number of block in the chain
    def size(self):
        return len(self.blocks)


    # This function count the number of entries for a given item in the blockchain

    def countitem(self, item):
        count = 0
        for i in range(1, len(self.blocks)):
            if self.blocks[i].evidenceID == item:
                count = count + 1
        return count

        # Print the given item of the blockchain
        # This will print the given item of the blockchain block in increasing order (older to recent)

    def loggivenitem(self, stop, item, revers):
        count = 0
        listentrie = []
        for i in range(1, len(self.blocks)):
            if self.blocks[i].evidenceID == item:
                count = count + 1
                listentrie.append(self.blocks[i])
        if revers == 'n':
            for i in range(1, stop):
                print('Case: ', listentrie[i].caseID)
                print('Item: ', listentrie[i].evidenceID)
                print('Action: ', listentrie[i].state)
                print('Time: ', listentrie[i].timestamp)
        elif revers == 'y':
            while stop > 0:
                print('Case: ', listentrie[i].caseID)
                print('Item: ', listentrie[i].evidenceID)
                print('Action: ', listentrie[i].state)
                print('Time: ', listentrie[i].timestamp)
                stop = stop - 1

    # Print the each block item of the blockchain
    # This will print all the blockchain bloc in increasing order (older to recent)

    def log(self, stop):
        for i in range(1, stop):
            print('Case: ', self.blocks[i].caseID)
            print('Item: ', self.blocks[i].evidenceID)
            print('Action: ', self.blocks[i].state)
            print('Time: ', self.blocks[i].timestamp)

        # Print the each block item of the blockchain in reverse order
        # This will print all the blockchain bloc in reverse order (recent to old)

    def logreverse(self, stop):
        while stop > 0:
            print('Case: ', self.blocks[stop].caseID)
            print('Item: ', self.blocks[stop].evidenceID)
            print('Action: ', self.blocks[stop].state)
            print('Time: ', self.blocks[stop].timestamp)
            stop = stop - 1

    # THis function Check in an previous registred item of the blockchain
    # Only check in an item if that item previouly exist in the blockchain and hd been check out.

    def checkin(self, itemid):
        exists = 0
        checks = 0
        j = len(self.blocks) - 1
        while j > 0:
            if self.blocks[j].evidenceID == itemid:
                exists = 1
                if self.blocks[j].state == 'CHECKEDOUT':
                    #self.blocks.append(Block.Block(len(self.blocks),
                     #                        self.blocks[len(self.blocks) - 1].hash,
                      #                       datetime.datetime.now().isoformat(),
                      #                       self.blocks[j].caseID, itemid, "CHECKEDIN", 14, "data",
                      #                       len(self.blocks) - 1))
                    print('Case: ', self.blocks[j + 1].caseID)
                    print('Checked out item: ', self.blocks[j + 1].evidenceID)
                    print('Status: ', self.blocks[j + 1].state)
                    print('Time of action: ', self.blocks[j + 1].timestamp)
                    break
                elif self.blocks[j].state == 'CHECKEDIN':
                    checks = 1
            j = j - 1
        if exists == 0:
            print("This item does not exist in the blockchain")
        elif checks == 1:
            print('Can not check in a checked in item. Must check it out first')

    # Checkout an existing block from the blockchain
    # Only check out an item if that item exists in the blockchain and had been check in
    def checkout(self, itemID):
        exist = 0
        check = 0
        for j in range(0, len(self.blocks)):
            if self.blocks[j].evidenceID == itemID:
                exist = 1
                if self.blocks[j].state == 'CHECKEDIN':
                  #  self.blocks.append(Block(len(self.blocks),
                   #                          self.blocks[len(self.blocks) - 1].hash,
                    #                         datetime.datetime.now().isoformat(),
                     #                        self.blocks[j].caseID, itemID, "CHECKEDOUT", 14, "data",
                      #                       len(self.blocks) - 1))
                    print('Case: ', self.blocks[len(self.blocks) - 1].caseID)
                    print('Checked out item: ', self.blocks[len(self.blocks) - 1].evidenceID)
                    print('Status: ', self.blocks[len(self.blocks) - 1].state)
                    print('Time of action: ', self.blocks[len(self.blocks) - 1].timestamp)
                elif self.blocks[j].state == 'CHECKEDOUT':
                    check = 1
        if exist == 0:
            print("This item does not exist in the blockchain")
        elif check == 1:
            print('Can not check out a checked out item. Must check it in first')

    # This function verify the following:
    # Verify if H(blocks[i]) is correctly stored in next block’s previous_hash.
    # if an item was attended to modified after been checkout

    def verify(self, isWrong=True):
        flag = True
        for i in range(1, len(self.blocks)):
            if i == 1 or i==2:#
                print('initial Block')
            elif hashing(self.blocks[i - 1]) != self.blocks[i].prevHash:  # check that previous and current hash match
                flag = False
               # print(binascii.hexlify(hashing(self.blocks[i - 1])) , binascii.hexlify(self.blocks[i].prevHash))
                if isWrong:
                    print("Transactions in blockchain: ", len(self.blocks))
                    print("State of blockchain: ERROR")
                    print("Bad block: ", i)
                    sys.exit("Block contents do not block checksum")
            elif self.blocks[i - 1].timestamp >= self.blocks[
                i].timestamp:  # Check if block time were registered accordinaly
                flag = False
                if isWrong:
                    print("Transactions in blockchain: ", len(self.blocks))
                    print("State of blockchain: ERROR")
                    print("Bad block: ", i)
                    sys.exit('Backdating at block')
        if flag:
            print("Transactions in blockchain: ", len(self.blocks) - 1)
            print("State of blockchain: CLEAN")

        return flag


STATE = {
    "init": b"INITIAL\0\0\0\0",
    "in": b"CHECKEDIN\0\0",
    "out": b"CHECKEDOUT\0",
    "dis": b"DISPOSED\0\0\0",
    "des": b"DESTROYED\0\0",
    "rel": b"RELEASED\0\0\0",
    "INITIAL": b"INITIAL\0\0\0\0",
    "CHECKEDIN": b"CHECKEDIN\0\0",
    "CHECKEDOUT": b"CHECKEDOUT\0",
    "DISPOSED": b"DISPOSED\0\0\0",
    "DESTROYED": b"DESTROYED\0\0",
    "RELEASED": b"RELEASED\0\0\0",
}