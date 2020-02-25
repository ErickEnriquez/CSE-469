#! /usr/bin/env python

# from Project_BlockChain import Blockcain
from Blockchain import Blockchain

# TEST
size = 0
bc = Blockchain()  # Create a blockchain object

text = input("enter a command or 'q' to quit: ")
inlist = text.split()

while inlist[0] != 'q':

    # Check number of arguments
    if len(inlist) < 1:
        print("This command is missing some argument")
        text = input("enter a command or 'q' to quit: ")
        inlist = text.split()

    # init command
    else:
        if inlist[0] == 'init':
            if size == 0:
                print("Great! You just Created your INITIAL block")
                size = 1
                # print("block size: " , size)
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()

            else:
                print("Blockchain file found with INITIAL block already")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()

        # Add command
        elif inlist[0] == 'add':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) < 5:
                print("This command has too few argument")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) % 2 == 0:
                print("This command is missing or too much argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            else:
                 for i in range(1, len(inlist)):
                    if inlist[i] == '-i':
                        bc.add(inlist[2], inlist[i + 1])  # add a block
                 size = bc.size()
                 print("block size: ", size)  # print size after adding a block
                 text = input("enter a command or 'q' to quit: ")
                 inlist = text.split()

        # verify command
        elif inlist[0] == 'verify':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) != 1:
                print("There is too much or too few argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            else:
                bc.verify()
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()

        # log command to print all blocks
        elif inlist[0] == 'log' and inlist[1] == '-n':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) < 3:  # ///////////////////////////////////////////T/////tO CHECK AGAIN
                print("There is too few argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) >= 5:
                item = inlist[4]
                count = bc.countitem(item)
                stop = int(inlist[2])
                if count < stop:
                    print("Number of occurence of this item in the blockchain is:  ", count)
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()
                else:
                    bc.loggivenitem(stop, item, 'n')
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()
            else:
                stop = int(inlist[2])
                if stop > bc.size():
                    print("Number of block in the blockchain is:  ", bc.size())
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()
                else:
                    bc.log(stop + 1)
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()

        # log reverse command to print all block
        elif inlist[0] == 'log' and inlist[1] == '-r':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) < 4:  # ///////////////////////////////////////////TO CHECK AGAIN
                print("There is too much or too few argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            else:
                stop = int(inlist[3])
                if stop > bc.size():
                    print("Number of block in the blockchain is:  ", bc.size())
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()
                else:
                    bc.logreverse(stop)
                    text = input("enter a command or 'q' to quit: ")
                    inlist = text.split()

        # checkout command
        elif inlist[0] == 'checkout':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) != 3:  # ///////////////////////////////////////////TO CHECK AGAIN
                print("There is too much or too few argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            else:
                bc.checkout(inlist[2])
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()

        # checkin command
        elif inlist[0] == 'checkin':
            if size == 0:
                print("No INITIAL block, create one  using 'init' first\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            elif len(inlist) != 3:  # ///////////////////////////////////////////TO CHECK AGAIN
                print("There is too much or too few argument in your command\n")
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
            else:
                bc.checkin(inlist[2])
                text = input("enter a command or 'q' to quit: ")
                inlist = text.split()
        else:
            print("UNKNOW COMMAND")
            text = input("enter a command or 'q' to quit: ")
            inlist = text.split()

print("done!!!!")
