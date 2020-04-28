#Larissa Pokam
#Erick Enriquez
#Zayne Bamond


# *-* coding: utf-8 *-*

import random
import re
import struct
import subprocess
import unittest
from collections import namedtuple
from copy import deepcopy as copy
from datetime import datetime, timedelta, timezone
from hashlib import sha1
from pathlib import Path
from shlex import split
from subprocess import PIPE, CalledProcessError
from sys import byteorder
from tempfile import TemporaryDirectory
from typing import BinaryIO, List, Callable
from uuid import UUID, uuid4
import math
import sys

import Block





block_head_fmt = "20s d 16s I 11s I"
block_head_len = struct.calcsize(block_head_fmt)
block_head_struct = struct.Struct(block_head_fmt)




#======================================================================
# packing the structure
#======================================================================
def pack_block(Block):
    if Block.timestamp == 0:
        stamp = 0
    else:
        stamp = datetime.timestamp(Block.timestamp) #create a timestamp
    case = Block.caseID.bytes #turn the UUID into big endian bytes
    temp = bytearray(case)  #turn the bytes into a byte array
    temp.reverse()  #reverse the bytes to be in little endian ordering
    try:
        block_bytes = block_head_struct.pack(
            bytes(Block.prevHash,encoding='utf-8'),#assuming this is a string
            stamp,
            temp,
            Block.evidenceID,
            Block.state,
            Block.dataLength,
           # Block.data  #Me
        )
    except struct.error:
        sys.exit('ERROR PACKING BLOCK')
    return block_bytes



##########################################################################
# Unpacking structure and returning a block object
##########################################################################

def unpack(block_bytes):
  
    try:
        block_contents = block_head_struct.unpack(block_bytes)
        #print(block_contents)
        temp = bytearray(block_contents[2])
        temp.reverse()
        temp = bytes(temp)
        #print('BLOCK DATA LENGTH ' , block_contents[5], type(block_contents[5]) )
    except struct.error:
        sys.exit('ERROR UNPACKING BLOCK')
    newBlock = Block.Block(
        block_contents[0],
        block_contents[1],
        UUID(bytes=temp),
        block_contents[3],
        block_contents[4],
        block_contents[5]
        #block_contents[6],   #Me
    )
    
    return newBlock


