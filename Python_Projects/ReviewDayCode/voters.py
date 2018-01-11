#!/usr/bin/python

"""
Created on Wed Nov  7 19:10:22 2012
@author: Therese Demers
@file: voters.py
"""



print "This is a voting simulation\n"

Ducky = 0
Monkey = 0

votingHappening = True

while(votingHappening):
    result = raw_input("Enter 1 to vote for Ducky, 2 to vote for Monkey and 0 to exit the voting simulation\n")
    if(int(result) == 1):
        Ducky = Ducky + 1
    elif(int(result) == 2):
        Monkey = Monkey + 1
    elif(int(result) == 0):
        votingHappening = False
    else:
        print "Didn't enter valid option.  Please learn how to read English and try again!\n"

print ("Ducky had {0} votes and Monkey had {1} votes\n".format(Ducky,Monkey))

if(Ducky > Monkey):
    print "Ducky wins!"
else:
    print "Monkey wins!"
