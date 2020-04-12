#!/usr/bin/env python3


import binascii
from BlockPack import unpack
from Block import Block
from uuid import UUID
import array

with open('data.bin' ,'rb') as fp:
    while True:
        bytes_data =  fp.read(68)
        if not bytes_data:
            break
        block  = unpack(bytes_data)
        block.dataLength = fp.read(block.dataLength)
        print('PREV HASH:' , block.prevHash)
        print('TIMESTAMP: ' , block.timestamp)
        print(block.caseID)
        print('CASE ID: ',  block.caseID , ' EXPECTED ' , 'fce7da5c-4994-45db-9440-0b872895db01' )
        print('EVIDENCE ID: ', block.evidenceID)
        print('STATE: ' , block.state)
        print('DATALENGTH: ', block.dataLength)
        print('DATA: ', block.data)
        print('\n\n\n\n\n\n\n')