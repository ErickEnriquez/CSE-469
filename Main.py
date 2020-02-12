from Blockchain import Blockchain


#TEST

#size = bc.size() #create an object
size = 0
print("size is: ")
print(size)  #print initial size
#print ("Status is: " + bc.)


text = input("enter your command: ")

inlist = text.split()

if len(inlist) < 2:
    print("This command is missing some argument")
else:
    if inlist[1] == 'init':
        if size == 0:
            bc = Blockchain()
            print("Great! You just Created your INITIAL block")
            size = bc.size()
            print(size)

        else:
            print("Blockchain file found with INITIAL block already")
    elif inlist[1] == 'add':
        if size == 0:
            print("No INITIAL block, create one  using 'init' first")
        elif len(inlist) < 6:
            print("This command has too few argument")
        elif len(inlist) % 2 != 0:
            print("This command is missing some argument")
        else:
            bc.add(inlist[3], inlist[5])  # add a block
            size = bc.size()
            print(size)  # print size after adding a block

print("done!!!!")