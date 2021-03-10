#!/bin/bash

make clean

make 

clear

./bchoc init

./bchoc add -c be844812-ab9a-4127-9f0f-d6d4d25fef00 -i 2842381549

./bchoc remove -i 2842381549 -y RELEASED