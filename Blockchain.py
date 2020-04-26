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


class Blockchain():

    # Blockchain Constructor
    def __init__(self):
        self.blocks = []  # create empty list to hold items


    # Add a new block to the chain and make sure there is no item duplicate
    def add(self, case, item, data):
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
                   0,
                   b'',   #Me
                ))
            else:
                self.blocks.append(Block.Block(
                                    str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                                    datetime.now(),                             #timestamp
                                    UUID(case),                                   #caseID
                                    item,                                   #evidence id
                                    STATE['in'],                            #state
                                    0,                                    #datalength
                                    data,                                   #data
                                     ))
            print('Case: ', self.blocks[len(self.blocks) - 1].caseID)
            print('item ID: ', self.blocks[len(self.blocks) - 1].evidenceID)
            print('Status: ', self.blocks[len(self.blocks) - 1].state.decode('utf-8'))
            print('Time of action: ', self.blocks[len(self.blocks) - 1].timestamp.isoformat())

 
    #this function will create list to be printed if -n is selected then it will pass it to parse_if_num_true() function
    #possible combinations, 
   
    '''
        r   n   c   i

        0   0   0   0       -DONE
        0   0   0   1       -DONE
        0   0   1   0       -DONE
        0   0   1   1       -DONE
        0   1   0   0       -D
        0   1   0   1       -D
        0   1   1   0       -D
        0   1   1   1       -D
        1   0   0   0       -DONE
        1   0   0   1       -DONE
        1   0   1   0       -DONE
        1   0   1   1       -DONE
        1   1   0   0       -D
        1   1   0   1       -D
        1   1   1   0       -D
        1   1   1   1       -D
            '''
    def parse_log_command(self,reverseFlag,numEntriesFlag , numEntries,caseIdFlag , caseId,evidenceIdFlag , evidenceId):
        list1 = []#create a empty list
        
        if reverseFlag == True: #if we have the reverse flag start by reversing entire list
            self.blocks.reverse()

        if numEntriesFlag == False and caseIdFlag == False and evidenceIdFlag == False: # if we only get log or log -r
            self.print_log_entries(self.blocks)
            return

        if numEntriesFlag == False: #if we don't have to worry about the num of entries handles all options where we don't select num entries
            if caseIdFlag == True and evidenceIdFlag == False:#only have a case id flag
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].caseID == uuid.UUID(caseId):
                     list1.append(self.blocks[i])
               # print("NUMBER OF BLOCKS THAT HAVE CORRECT CASE ID", len(list1))
                
            elif evidenceIdFlag == True and caseIdFlag == False:#if we have evidence id only
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].evidenceID == int(evidenceId):
                        list1.append(self.blocks[i])
                #print("NUMBER OF BLOCKS THAT HAVE CORRECT EVIDENCE ID " , len(list1))
            elif evidenceIdFlag == True and caseIdFlag == True:
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].evidenceID == int(evidenceId) and self.blocks[i].caseID == uuid.UUID(caseId):
                        list1.append(self.blocks[i])
                #print("NUMBER OF BLOCKS THAT HAVE CORRECT CASE ID AND EVIDENCE ID ", len(list1))
            if len(list1) == 0:# if we have no matches , just return and don't print
               return
            self.print_log_entries(list1)
            return

        if numEntriesFlag == True:
          self.parse_if_num_true(reverseFlag,numEntriesFlag,numEntries,caseIdFlag,caseId,evidenceIdFlag,evidenceId)


    # this function goes through all 8 options if the user selects -n flag
    def parse_if_num_true(self,reverseFlag,numEntriesFlag , numEntries,caseIdFlag , caseId,evidenceIdFlag , evidenceId):
        list1 = []
        if int(numEntries) > len(self.blocks):  #if the user enters a number larger than the size of the blockchain
            sys.exit('Error you entered a number larger than the number of blocks')
        else:
            if caseIdFlag == False and evidenceIdFlag == False:
                for i in range(0,int(numEntries)):
                    list1.append(self.blocks[i])
            elif caseIdFlag == True and evidenceId == False:
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].caseID == uuid.UUID(caseId):
                        list1.append(self.blocks[i])
            elif caseIdFlag == False and evidenceIdFlag == True:
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].evidenceID == int(evidenceId):
                        list1.append(self.blocks[i])
            elif caseIdFlag == True and evidenceIdFlag == True:
                for i in range(0,len(self.blocks)):
                    if self.blocks[i].evidenceID == int(evidenceId) and self.blocks[i].caseID == uuid.UUID(caseId):
                        list1.append(self.blocks[i])
            if len(list1) == 0:
                return
            elif int(numEntries) > len(list1):
                list2 = list1
            else:
                list2 = list1[:int(numEntries)]
            self.print_log_entries(list2)


       



    def print_log_entries(self,arr):
        for i in range(0,len(arr)):
            print('Case: ', arr[i].caseID)
            print('Item: ', arr[i].evidenceID)
            print('Action: ', arr[i].state.decode('utf-8'))
            print('Time: ',  datetime.fromtimestamp(arr[i].timestamp)) 
            if i < (len(arr)-1):
                print('\n')


    # THis function Check in an previous registred item of the blockchain
    # Only check in an item if that item previouly exist in the blockchain and hd been check out.

    def checkin(self, itemid,data):
        exists = 0
        j = len(self.blocks) - 1
        while j > 0:
            if self.blocks[j].evidenceID == int(itemid):
                exists = 1
                if self.blocks[j].state == STATE['out']: # if the block contains the evidence ID and it has a state of 'checkout'
                    self.blocks.append(Block.Block(
                            str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                            datetime.now(),                                  #timestamp
                            self.blocks[j].caseID,                           #caseID
                            itemid,                                          #evidence id
                            STATE['in'],                                     #state
                            0,                                                #datalength
                            b'',                                            #data
                                     ))
                    print('Case: ', self.blocks[j + 1].caseID)
                    print('Checked in item: ', self.blocks[j + 1].evidenceID)
                    print('Status: ', self.blocks[j + 1].state)
                    print('Time of action: ', self.blocks[j + 1].timestamp)
                    return
                elif self.blocks[j].state == STATE['in'] or self.blocks[j].state == STATE['dis'] or self.blocks[j].state == STATE['des'] or self.blocks[j].state == STATE['rel'] or self.blocks[j].state == STATE['init']  :
                    sys.exit('Evidence must be checked out first before checkin')
            j = j - 1
        if exists == 0:
            sys.exit("This item does not exist in the blockchain")

    # Checkout an existing block from the blockchain
    # Only check out an item if that item exists in the blockchain and had been check in
    def checkout(self, itemid,data):
        exists = 0
        j = len(self.blocks) - 1
        while j > 0:
            if self.blocks[j].evidenceID == int(itemid):
                exists = 1
                if self.blocks[j].state == STATE['in']: # if the block contains the evidence ID and it has a state of 'checkout'
                    self.blocks.append(Block.Block(
                            str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                            datetime.now(),                                  #timestamp
                            self.blocks[j].caseID,                           #caseID
                            itemid,                                          #evidence id
                            STATE['out'],                                     #state
                            0 ,                                               #datalength
                            b'',                                           #data
                                     ))
                    print('Case: ', self.blocks[j + 1].caseID)
                    print('Checked out item: ', self.blocks[j + 1].evidenceID)
                    print('Status: ', self.blocks[j + 1].state)
                    print('Time of action: ', self.blocks[j + 1].timestamp)
                    return
                elif self.blocks[j].state == STATE['out'] or self.blocks[j].state == STATE['dis'] or self.blocks[j].state == STATE['des'] or self.blocks[j].state == STATE['rel'] or self.blocks[j].state == STATE['init']  :
                    sys.exit('Evidence must be checked in first before checkout')
            j = j - 1
        if exists == 0:
            sys.exit("This item does not exist in the blockchain")

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

    # remove an existing block from the blockchain
    # Only remove an item if that item exists in the blockchain and had been check in
    def remove (self, itemid, status, data):
        exists = 0

        #retrieve the first 3 leters of the status
        count = 0
        stat = ''
        while (count < 3): 
            stat = stat + status[count]
            count = count + 1
        reason = stat.lower()

        if reason == 'dis' or reason == 'des' or reason == 'rel':
            j = len(self.blocks) - 1
            while j > 0:
                if self.blocks[j].evidenceID == int(itemid):
                    exists = 1
                    if self.blocks[j].state == STATE['in']: # if the block contains the evidence ID and it has a state of 'checkin'
                        if data == b'':
                            self.blocks.append(Block.Block(
                                str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                                datetime.now(),                                  #timestamp
                                self.blocks[j].caseID,                           #caseID
                                itemid,                                          #evidence id
                                STATE[reason],                                     #state
                                0 ,                                              #datalength
                                b'',                                   #data
                                        ))
                        else:
                            self.blocks.append(Block.Block(
                                str(hashing(self.blocks[len(self.blocks) - 1])), #prev hash
                                datetime.now(),                                  #timestamp
                                self.blocks[j].caseID,                           #caseID
                                itemid,                                          #evidence id
                                STATE[reason],                                     #state
                                len(data) ,                                              #datalength
                                data.encode(),                                   #data
                                        ))
                                            
                        print('Case: ', self.blocks[j + 1].caseID)
                        print('Removed item: ', self.blocks[j + 1].evidenceID)
                        print('Status: ', self.blocks[j + 1].state)
                        #print the owner infos if the reason is RELEASED
                        if status == STATE['rel']: 
                            print('Owner info: ', self.blocks[j + 1].data)  #Me
                        print('Time of action: ', self.blocks[j + 1].timestamp)
                                                
                        return
                    elif self.blocks[j].state == STATE['out'] or self.blocks[j].state == STATE['dis'] or self.blocks[j].state == STATE['des'] or self.blocks[j].state == STATE['rel'] or self.blocks[j].state == STATE['init']  :
                        sys.exit('Evidence must be checked in first before remove')
                j = j - 1
        else:
            sys.exit('Invalid remove reason (why) input')
        if exists == 0:
            sys.exit("This item does not exist in the blockchain")


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