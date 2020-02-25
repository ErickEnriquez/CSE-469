#!/bin/bash

CWD=$(pwd) #store the current working directory

touch $HOME/.bash_profile

echo 'export PATH=$PATH:'$CWD > $HOME/.bash_profile #store the location of the executables in a bash_profile file 

cp $CWD/Main.py $CWD/bchoc #copy the main python file into a bchoc executable

chmod +x bchoc #make the bchoc executable

#make sure you run make this script as sudo and restart terminal after using 