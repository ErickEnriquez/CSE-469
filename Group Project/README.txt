# CSE469Project

Team name:
    Erick Enriquez   1208001804  
    Zayne Bamond     1202500836  
    Larissa Pokam   1213998902 
  
Project Name: Blockchain Chain of Custody

Project Description: THis project is the Implementation of the chain of custody form.
    The Chain of Custody form is a critical element to a forensic investigation because examiners use it to record the history
    of the evidence from the time it is found until the case is closed or goes to court. We used Blockchaain as a tool here 
    because it will help to preserved the integrity of the Chain of Custody. So if the document is contaminated it will dentify
    the responsible individual. In general the Chain of Custody form keeps track of three pieces of important information (in
    addition to all the details that uniquely identify the specific piece of evidence): where the evidence was stored, who had
    access to the evidence and when, ans what actions were done to the evidence.

OS: LInux (Ubuntu 18.04 64 bit)
Programming Language: Python
Compiler: ghc, ghc-dynamic
Excecutable: bchoc

All files used:
    bchoc: this file is the Excecutable file
    Main.py: this class is is the main class that drive the test
    block.py: content all the element to represent a block.
    BlockPack.py: this class allw to pack and unpack a block.
    demoBlock.py: this class content the block structure and the parameter structure.
    Blockchain.py: this class content the actual Implementation of the blockchain function.
    Makefile: this is file containing a set of directives used by 'make' command to build automate tests.
    readTest.py: this is a simple little program that you can use to test to output the contents of the block file
    
Function Implemented:
    add: Add a new evidence item to the blockchain and associate it with the given case identifier. 
        dd a new checkout entry to the chain of custody for the given evidence item.
    checkin: Add a new checkin entry to the chain of custody for the given evidence item. 
    log: Display the blockchain entries giving the oldest first (unless -r is given).
    remove: Prevents any further action from being taken on the evidence item specified.
    init: Sanity check. Only starts up and checks for the initial block.
    verify: Parse the blockchain and validate all entries.
    
 Parameter Used:
     c case_id: Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log 
        only blocks with the given case_id are returned.
    -i item_id: Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned. The item  
         ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.
    -r, --reverse: Reverses the order of the block entries to show the most recent entries first.
    -n num_entries: When used with log, shows num_entries number of block entries.
    -y reason, --why reason: Reason for the removal of the evidence item. Must be one of: DISPOSED, DESTROYED, or RELEASED. If the reason 
        given is RELEASED, -o must also be given.

    -o owner: Information about the lawful owner to whom the evidence was released. At this time, text is free-form and does not have 
        any requirements.

How does the program works:
    The way that this software needs to start is that when you first use the software the system should go through, check if there is
    a binary file that already has the initial seed block that is needed by the blockchain. The fields that this, as well as every other
    block in the blockchain, should have to include Previous hash, Timestamp, CaseID, Evidence ID, State, Data Length, and Data If the 
    system cannot find this binary file then the first thing that should be done is that the software should create a binary file at   
    BCHOC_FILE_PATH. After this file is created the system should then go through and create the initial seed block of the chain with 
    the data that was specified in the project requirements. After this is done the data should be serialized into a series of bytes, 
    and those bytes should be then written to the binary file. From here the program executed each given function following the given 
    function functionality.
        When a person wants to enter a new block into the blockchain the steps that are required are followed. First, the system should 
    go through and verify that the options that the user passes are valid, after this it should check if there is a valid blockchain,
    if there is none then the software should create the initial block, after this the system should then go about and ensure that a 
    his case ID and evidence ID is not already in the blockchain, if not then it should create a new block using the data that the user 
    entered. The SHA1 hash of the last block should then be computed and set as the prev hash of the new block, as well as setting the 
    timestamp for when the new block was created. After this is done the system should go through and serialize any new blocks that were 
    created into bytes and append them to the binary file. 




