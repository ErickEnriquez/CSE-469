#!/usr/bin/env python3

 
#this is a simple little program that you can use to test to output the contents of the block file

import binascii
from BlockPack import unpack
from Block import Block
import datetime


with open('data.bin' ,'rb') as fp:
    while True:
        bytes_data =  fp.read(68)
        if  len(bytes_data) is not 68:
            break
        else:
            block  = unpack(bytes_data)
            block.dataLength = fp.read(block.dataLength)
            print("Previous hash: ", block.prevHash)
            print("Timestamp: ", datetime.datetime.fromtimestamp(block.timestamp))
            print('Case ID: ', block.caseID)
            print('Evidence ID: ')
            print('State: ', block.state)
            print('Data length: ', block.dataLength)
            print('Data: ', block.data)