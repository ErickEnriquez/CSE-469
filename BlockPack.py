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
    stamp = datetime.timestamp(Block.timestamp) #create a timestamp

    block_bytes = block_head_struct.pack(
        Block.prevHash,
        stamp,
        Block.caseID.bytes_le,
        Block.evidenceID,
        Block.state,
        Block.dataLength
        
    )
    return block_bytes

def pack_inital_block(Block):
    block_bytes = block_head_struct.pack(
        bytes(Block.prevHash),
        Block.timestamp,
        Block.caseID.to_bytes(16,'little'),
        Block.evidenceID,
        Block.state,
        Block.dataLength,
    )
    
    return block_bytes

##########################################################################
# Unpacking structure and returning a block object
##########################################################################

def unpack(block_bytes):
    try:
        block_contents = block_head_struct.unpack(block_bytes)
    except struct.error:
        print('ERROR UNPACKING')
    newBlock = Block.Block(
        block_contents[0],
        block_contents[1],
        block_contents[2],
        block_contents[3],
        block_contents[4],
        block_contents[5]
    )
    return newBlock










#======================================================================
# Unpacking the block structure
#======================================================================
#fp = open('data.bin','rb')
#block = fp.read(68)
#blockContents = block_head_struct.unpack(block)
#timestamp = datetime.fromtimestamp(blockContents[1])
#datalen = blockContents[5]
#data = fp.read(datalen)
#data = data.decode('utf-8')
#print(data)
#print(timestamp)
#print(blockContents)

#fp.close()

