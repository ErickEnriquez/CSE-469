# CSE_469_Homework1


Erick Enriquez

ASU ID: 1208001804

This is an exercise in being able to read in hex values from a master boot record, hashing and checking hashes, and determining types of partitions on a drive given raw data file  

when called the makefile creates a script called mbr_info and then it sets the script as executable using the chmod +x command 


Once you start the script first we open the file, and hash the file with md5 and sha1, then we create the text files and write the hashes to them , next we take the 512 bytes and convert them to hex by using the binascii library and the .hexify function, which takes the 512 bytes and creates 1024 length string then we go past the first 446 bytes of bootloader code and read the master boot record

we go through each of the partitions and caculate the size and the starting address and the hex value by converting to Big Endian and converting to decimal number when needed

we then open up the csv and find the hex code of the partition type, and after we calculate the address for the last 8 bytes of the boot record by doing (LBA * 512) + 504 and reading next 8 bytes which are the master boot record and we display them

