#!/bin/bash
clear

make clean

make 

make init_test

make add_1_more

make add_one_test

./readTest.py