# CSE469Project

Team name:
  Larissa Pokam Epse Takou, 1213998902
  Erick Enriquez, 
  Zayne Bamond
  
Project: Blockchain Chain of Custody
Project Description: THis project is the Implementation of the chain of custody form.
    The Chain of Custody form is a critical element to a forensic investigation because examiners use it to record the history
    of the evidence from the time it is found until the case is closed or goes to court. We used Blockchaain as a tool here 
    because it will help to preserved the integrity of the Chain of Custody. So if the document is contaminated it will dentify
    the responsible individual. In general the Chain of Custody form keeps track of three pieces of important information (in
    addition to all the details that uniquely identify the specific piece of evidence): where the evidence was stored, who had
    access to the evidence and when, ans what actions were done to the evidence.

OS: LInux (Ubuntu 18.04 64 bit)
Programming Language: Python
Excecutable: bchoc

Function Implemented:
    add: Add a new evidence item to the blockchain and associate it with the given case identifier. 
    checkout: Add a new checkout entry to the chain of custody for the given evidence item.
    checkin: Add a new checkin entry to the chain of custody for the given evidence item. 
    log: Display the blockchain entries giving the oldest first (unless -r is given).
    remove: Prevents any further action from being taken on the evidence item specified.
    init: Sanity check. Only starts up and checks for the initial block.
    verify: Parse the blockchain and validate all entries.
    
 Command Used:
     c case_id: Specifies the case identifier that the evidence is associated with. Must be a valid UUID. When used with log 
  only blocks with the given case_id are returned.

    -i item_id: Specifies the evidence item’s identifier. When used with log only blocks with the given item_id are returned.   The item ID must be unique within the blockchain. This means you cannot re-add an evidence item once the remove action has been performed on it.

    -r, --reverse: Reverses the order of the block entries to show the most recent entries first.

    -n num_entries: When used with log, shows num_entries number of block entries.

    -y reason, --why reason: Reason for the removal of the evidence item. Must be one of: DISPOSED, DESTROYED, or RELEASED. If the reason given is RELEASED, -o must also be given.

      -o owner: Information about the lawful owner to whom the evidence was released. At this time, text is free-form and     
    does not have any requirements.

# startup
run the setup.sh file as sudo to install the path variable and create the bchoc initially, make sure that the setup file has its executable flag as on, you may need to restart the terminal to for changed to take effect

