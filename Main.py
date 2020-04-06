#! /usr/bin/env python3

# from Project_BlockChain import Blockcain
#from Blockchain import Blockchain
import argparse  # parsing sys.argv line args
import os
import sys
#bc = Blockchain()  # Create a blockchain object

##############################################################
# check if the file exists
##############################################################
file_exists = True
try:
    fp = open('data.bin','rb')
except IOError:
    file_exists = False
finally:
    fp.close()

print('file found = ', file_exists)


arguments = sys.argv[1:]  # grab everything in list except executable name


parser = argparse.ArgumentParser()  # parser object


if sys.argv[1] == "init":
    # init stuff here
    print("Sanity check. Only starts up and checks for the initial block.")
elif sys.argv[1] == 'verify':
    # verify code here
    print("Parse the blockchain and validate all entries.")
elif sys.argv[1] == 'add':
    parser.add_argument('add', help="Add a new evidence item to the blockchain and associate it with the given case identifier. For users convenience, more than one item_id may be given at a time, which will create a blockchain entry for each item without the need to enter the case_id multiple times. The state of a newly added item is CHECKEDIN. The given evidence ID must be unique(i.e., not already used in the blockchain) to be accepted.")
    parser.add_argument('-c', help="Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log only blocks with the given case_id are returned.")
    # makes a list of the remaining numbers
    parser.add_argument('-i', nargs=argparse.REMAINDER, help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item_ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    print(args.i)
elif sys.argv[1] == 'checkin':
    parser.add_argument(
        'checkin', help="Add a new checkin entry to the chain of custody for the given evidence item. Checkin actions may only be performed on evidence items that have already been added to the blockchain.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    print(args.i)  # args.i holds the value of the itme ID
elif sys.argv[1] == 'checkout':
    parser.add_argument(
        'checkout', help="Add a new checkout entry to the chain of custody for the given evidence item. Checkout actions may only be performed on evidence items that have already been added to the blockchain.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    args = parser.parse_args(arguments)
    print(args.i)  # args.i holds the value of the itme ID
elif sys.argv[1] == 'log':
    parser.add_argument('log', help="Display the blockchain entries giving the oldest first (unless -r is given).")
    parser.add_argument('-r', '--reverse',
                        help="Reverses the order of the block entries to show the most recent entries first.")  # optional arg
    parser.add_argument('-n',
                        help="When used with log, shows num_entries number of block entries.")  # optional arg
    parser.add_argument('-c', help="Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log only blocks with the given case_id are returned.")  # optional arg
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")  # optional arg
    args = parser.parse_args(arguments)
    if args.reverse:
        print("you want the chain reversed")
    if args.n:
        print("you want the number of entries")
    if args.c:
        print("you want the only the blocks that contain this case ID")
    if args.i:
        print("you only want the blocks that contain this item ID")
elif sys.argv[1] == 'remove':
    parser.add_argument('remove', help="Prevents any further action from being taken on the evidence item specified. The specified item must have a state of CHECKEDIN for the action to succeed.")
    parser.add_argument('-i', help="Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.")
    parser.add_argument(
        '-y', '--why', help="Reason for the removal of the evidence item. Must be one of: DISPOSED, DESTROYED, or RELEASED. If the reason given is RELEASED, -o must also be given.")
    parser.add_argument(
        '-o', help="Information about the lawful owner to whom the evidence was released. At this time, text is free-form and does not have any requirements.")
    print('remove')
