#Larissa Pokam
#Erick Enriquez
#Zayne Bamond

#!/usr/bin/env python3

import argparse  # parsing sys.argv line args
import os
import sys
import os.path
import Block
from Block import printBlock
from BlockPack import pack_block,unpack#functions I created to pack and unpack a block
from Blockchain import Blockchain
import datetime






#os.environ['BCHOC_FILE_PATH'] = 'data.bin' #THIS IS HERE FOR TESTING, NEEDS TO BE COMMENTED OUT WHEN SUBMITTING

bc = Blockchain()   #initialize the blockchain

arguments = sys.argv[1:]  # grab everything in list except executable name


parser = argparse.ArgumentParser()  # parser object

############################################################################################################
#checks if the inital block exists, if not it creates inital block and returns false
def check_if_initial_block(file_path , bc):
    if os.path.exists(os.environ['BCHOC_FILE_PATH']):
        return True
    else:
        initial_block = Block.create_initial_block() # create initial block
        block_bytes= pack_block(initial_block) #pack the inital block into bytes
        with open(os.environ['BCHOC_FILE_PATH'],'wb') as fp:   #open a file to store block
            fp.write(block_bytes)#write the initial block to binary file
            fp.write(initial_block.data) # write the block data to file (make sure the string is in bytes)
        print('Blockchain file not found. Created INITIAL block.')
        bc.blocks.append(initial_block)
        return False

##############################################################################################################


def build_blockchain_from_file(bc):
    with open(os.environ['BCHOC_FILE_PATH'] ,'rb') as fp:
        while True:
            bytes_data =  fp.read(68)
            if  len(bytes_data) is not 68:
                break
            else:
                block  = unpack(bytes_data)
                block.data = fp.read(block.dataLength).decode('utf-8')
              #  print('\n\n')
              #  print("Previous hash: ", block.prevHash)
              #  print("Timestamp: ", datetime.datetime.fromtimestamp(block.timestamp))
              #  print('Case ID: ', block.caseID)
              #  print('Evidence ID: ', block.evidenceID)
              #  print('State: ', block.state)
              #  print('Data length: ', block.dataLength)
              #  print('Data: ', block.data)
              #  print('\n\n')
                bc.blocks.append(block)
    return bc


#======================================================================================================================================================

#simple utility function that will open the file and append the block passed to it
def write_to_file(block):
    with open(os.environ['BCHOC_FILE_PATH'] ,'ab') as fp:
       block_bytes = pack_block(block)
       fp.write(block_bytes)
       fp.write(block.data)


#=======================================================================================================================================================



if sys.argv[1] == "init":
 
    if len(sys.argv) > 2: #make sure we aren't adding extra arguments
        sys.exit('Invalid Parameters')
    if os.path.exists(os.environ['BCHOC_FILE_PATH']) == False:# if file doesn't exist
        initial_block = Block.create_initial_block() # create initial block
        #printBlock(initial_block)
        block_bytes= pack_block(initial_block) #pack the inital block into bytes
        with open(os.environ['BCHOC_FILE_PATH'],'wb') as fp:   #open a file to store block
            fp.write(block_bytes)#write the initial block to binary file
            fp.write(initial_block.data) # write the block data to file (make sure the string is in bytes)
        print('Blockchain file not found. Created INITIAL block.')
    else:#no blockchain file , need to create one with initial block
         with open(os.environ['BCHOC_FILE_PATH'],'rb') as fp:
           block_bytes = fp.read(68) #read 68 bytes of struct header
           initial_block = unpack(block_bytes)  #unpack the bytes and return a block object
           #printBlock(initial_block)
         print('Blockchain file found with INITIAL block.')
       


#=======================================================================================================================================================
elif sys.argv[1] == 'verify':
    # verify code here
    bc  = build_blockchain_from_file(bc)
    bc.verify()
#=======================================================================================================================================================



elif sys.argv[1] == 'add':
    parser.add_argument('add', help="Add a new evidence item to the blockchain and associate it with the given case identifier. For users convenience, more than one item_id may be given at a time, which will create a blockchain entry for each item without the need to enter the case_id multiple times. The state of a newly added item is CHECKEDIN. The given evidence ID must be unique(i.e., not already used in the blockchain) to be accepted.")
    parser.add_argument('-c', help="Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log only blocks with the given case_id are returned.")
    # makes a list of the remaining numbers
    parser.add_argument('-i', action='append', nargs='+', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item_ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    if args.c is None:
        sys.exit('PLEASE SUPPLY CASE ID')
    elif args.i is None:
        sys.exit('PLEASE SUPPLY A EVIDENCE ID')
    #--------------------------------------------------------------------
    result =  check_if_initial_block(os.environ['BCHOC_FILE_PATH'], bc)
    #--------------------------------------------------------------------
    if result == True: # if we have an initial blockchain already then load it into the data structure
        with open(os.environ['BCHOC_FILE_PATH'], 'rb') as fp:
           while True:
               block_bytes = fp.read(68)
               if len(block_bytes) is not 68:#if don't hav 68 bytes in the buffer we are done reading file
                   break
               else:
                temp_block = unpack(block_bytes)
                #print(temp_block.dataLength)
                temp_block.data = fp.read(temp_block.dataLength)
                bc.blocks.append(temp_block)
    sizebefore = len(bc.blocks)#store the length of the blockchain from before so we only append the new items
    
    for j in range(0,len(args.i)):
        bc.add(args.c,args.i[j][0],b'')   #Me
    with open(os.environ['BCHOC_FILE_PATH'],'ab') as fp:
         for i in range (sizebefore,len(bc.blocks)):
            block_bytes= pack_block(bc.blocks[i])
            #print(block_bytes)
            fp.write(block_bytes)
            fp.write(bc.blocks[i].data)

#=======================================================================================================================================================


elif sys.argv[1] == 'checkin':
    parser.add_argument(
        'checkin', help="Add a new checkin entry to the chain of custody for the given evidence item. Checkin actions may only be performed on evidence items that have already been added to the blockchain.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    bc = build_blockchain_from_file(bc) # build the blockchain file
    sizeBefore = len(bc.blocks) #get the size of the file before we add any new blocks
    bc.checkin(args.i,b'')  #add the block to the data structure
    for i in range(sizeBefore,len(bc.blocks)): # loop through and add append all of the new added blocks into the chain
        write_to_file(bc.blocks[i])

    

#=======================================================================================================================================================

elif sys.argv[1] == 'checkout':
    parser.add_argument(
        'checkout', help="Add a new checkout entry to the chain of custody for the given evidence item. Checkout actions may only be performed on evidence items that have already been added to the blockchain.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    bc = build_blockchain_from_file(bc) # build the blockchain file
    sizeBefore = len(bc.blocks) #get the size of the file before we add any new blocks
    bc.checkout(args.i,b'')
    for i in range(sizeBefore,len(bc.blocks)):
        write_to_file(bc.blocks[i])

#=======================================================================================================================================================

elif sys.argv[1] == 'log':
    parser.add_argument('log', help="Display the blockchain entries giving the oldest first (unless -r is given).")
    parser.add_argument('-r', '--reverse',
                        help="Reverses the order of the block entries to show the most recent entries first.",action='store_true')  # optional arg for reversing the list
    parser.add_argument('-n',
                        help="When used with log, shows num_entries number of block entries.")  # optional arg
    parser.add_argument('-c', help="Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log only blocks with the given case_id are returned.")  # optional arg
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")  # optional arg
    args = parser.parse_args(arguments)
    bc = build_blockchain_from_file(bc) # build the blockchain file

    reverseFlag = False
    numEntriesFlag = False
    caseIdFlag = False
    itemIdFlag = False

    if args.reverse:
        reverseFlag = True
    if args.n:
        numEntriesFlag = True
    if args.c:
        caseIdFlag = True
    if args.i:
        itemIdFlag = True
    bc.parse_log_command(reverseFlag,numEntriesFlag,args.n,caseIdFlag,args.c,itemIdFlag,args.i)
    #bc.log()

#=======================================================================================================================================================

elif sys.argv[1] == 'remove':
    parser.add_argument('remove', help="Prevents any further action from being taken on the evidence item specified. The specified item must have a state of CHECKEDIN for the action to succeed.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    parser.add_argument(
        '-y', '--why', help="Reason for the removal of the evidence item. Must be one of: DISPOSED, DESTROYED, or RELEASED. If the reason given is RELEASED, -o must also be given.")
    if sys.argv[5] == 'RELEASED':
        parser.add_argument(
            '-o', help="Information about the lawful owner to whom the evidence was released. At this time, text is free-form and does not have any requirements.")
    args = parser.parse_args(arguments)
    #print( "THIS IS THE EVIDENCE ID ", args.i , "\nThis is the why reason" , args.why , "\nThis is the -owner if applicable " , args.o)
    #what you have to do first is call the function that will read the file and then store it in bc object
    bc = build_blockchain_from_file(bc) # build the blockchain file
    
    #TO DO , develop the bc.remove function and then call it with the args that it needs
    sizeBefore = len(bc.blocks) #get the size of the file before we add any new blocks

    #if the reason is RELEASED we sent the owner infos else nothing
    if sys.argv[5] == 'RELEASED':
        bc.remove(args.i, args.why, args.o)
    else:
        bc.remove(args.i, args.why, b'')
    for i in range(sizeBefore,len(bc.blocks)):
        write_to_file(bc.blocks[i])


#=======================================================================================================================================================


