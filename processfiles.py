#!/usr/bin/python3
import os
import warnings
import sys
import time

os.system("ps -a > myProcess.txt")
newfiles = open("myData.txt", "w")
with open ("myProcess.txt", "r+") as outfile:
    for line is outfile:
        parts = line.split()
        newfiles.write(parts[0] + "\t" + parts[3] + "\n")
outfile.close()
time.sleep(10)
os.system('rm myProcess.txt')
newfiles.close()