#!/usr/bin/env python
import sys      # reading command line args
import os       # splits strings 
import hashlib  # hashing library
import binascii # reading file in hex
import csv      #for reading in the csv of the boot types


#checks the parition type byte by looking at the Partition Types.csv doc
def find_partition_type(byte):
    with open('PartitionTypes.csv') as CSVFile:
        reader = csv.reader(CSVFile,delimiter = ',')
        for row in reader:
            if row[0] == byte : #if we find the right partition hex code
                return row[1]   #return the name of the parition


#takes a little endian string of values. and returns the big endian string representation
def convert_little_to_big_endian(data):
    BigEndian = bytearray.fromhex(data)#convert the big endian to do math on the number
    BigEndian.reverse()#reverse the array
    BigEndian_String = ''.join(format(x, '02x') for x in BigEndian)#format the string back and remove the byte array part
    return BigEndian_String

#takes a hex string and converts it into a decimal number with 10 digits and adds padding if needed
def convert_hex_to_decimal_string(data):
    number = int(data,16)
    s = str(number)
    return s.zfill(10)

def last_8_bytes(address , filename):#gets last 8 bytes of boot record given address and the filename
    data = 0
    with open(filename,"rb")as filehandler:
        filehandler.seek(address,0)#go to the address offset that we need
        last8 = filehandler.read(8)#read the last 8 bytes
        data=last8
    data = binascii.hexlify(data)
    data = data.upper()
    output = ''
    i =0
    while i < 16 :
        output = output + " "  + data[i:i+2]
        i+=2

    return output

filename = sys.argv[1] #get the name of the file

BLOCK_SIZE = 512 # size of the block we will be reading while hashing

Md5file = "MD5-" + filename
ShaFile  = "SHA1-" +filename

#don't need to remove the extension just can add .txt extenstion at the end
#Md5file = os.path.splitext(Md5file)[0]# remove the .raw extension
#ShaFile = os.path.splitext(ShaFile)[0]# remove .raw extension

Md5file = Md5file + '.txt'
ShaFile = ShaFile + '.txt'


#hash the file with SHA 1
file_hash_obj = hashlib.sha1()
file_hash_MD5 = hashlib.md5()
with open(filename, 'rb') as f:
    fb = f.read(BLOCK_SIZE)
    data = fb #read first 512 bytes of data of master boot record
    while len(fb) > 0:
        file_hash_obj.update(fb)
        file_hash_MD5.update(fb)
        fb = f.read(BLOCK_SIZE)

#write the result into the file
with open(ShaFile,'w') as FileHandler:
    FileHandler.write(file_hash_obj.hexdigest())

#write the MD5 result into the file
with open(Md5file,'w') as FileHandler:
    FileHandler.write(file_hash_MD5.hexdigest())

#variables to help keep the byte sizes easier to read
offset  = 446 * 2
byte = 2 
word = 4 * 2
doubleword = 8 * 2
partitionlength = 16 * 2

dataString = binascii.hexlify(data) # make the data we have into a hex string

partitionNumber = 1
partition_address = []
partition_size = []
partition_type = []

while(offset < 1020 ) :# while we we haven't finished the parition
    partition = dataString[offset: offset + partitionlength] #grab the 16 bytes of the partition
    paritiontype = partition[word:word+byte] # grab the partition type
    startingsectorle = partition[doubleword:doubleword + word] # grab the 4 byte starting sector
    sizeLittle = partition[doubleword + word : partitionlength] # grab the 4 byte sector count

    Address = convert_little_to_big_endian(startingsectorle)#convert the starting address to big endian
    Size =convert_little_to_big_endian(sizeLittle)# convert the size to big endian

    StartingAddress = convert_hex_to_decimal_string(Address) #convert this to decimal string
    SizeString = convert_hex_to_decimal_string(Size)        #convert this to decimal String

    partition_address.append(int(StartingAddress,10))#store the starting address
    partition_size.append(int(SizeString,10))#store the size of the partition
    partition_type.append(paritiontype)

    if paritiontype != '00' :    #don't print our the empty partition
        output_data = paritiontype + " " + find_partition_type(paritiontype) + " " + StartingAddress + " " + SizeString
        print(output_data)#print the data 

    offset = offset + partitionlength # move 16 bytes to next partition

masterbootRecord_info = (partition_address,partition_size,partition_type)#strore the info as a tuple
for i in range(0,5):
    if masterbootRecord_info[2][i-1] != '00':   #if the partition number is empty
        print("Partition Number " + str(i))
        addr =  (masterbootRecord_info[0][i-1] *512) + 504 #size *address      
        print("Last 8 bytes of boot record:"+str(last_8_bytes(addr,filename)))
       



