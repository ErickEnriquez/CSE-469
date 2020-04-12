#!/usr/bin/env python3


import binascii
from BlockPack import unpack
from Block import Block
from uuid import UUID


with open('data.bin' ,'rb') as fp:
    counter = 1
    while True:
        bytes_data =  fp.read(68)
        if  len(bytes_data) is not 68:
            break
        else:
            block  = unpack(bytes_data)
            block.dataLength = fp.read(block.dataLength)