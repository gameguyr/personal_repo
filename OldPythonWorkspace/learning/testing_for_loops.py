#!/usr/bin/env python
#testing_for_loop

names=['sun','mercury','venus','earth','mars','jupiter'
,'saturn','uranus','neptune']

friends=['ramzi', 'mike', 'Vee', 'eric']

for j in range(0, len(friends)):
   # print j
   # print '\n', friends[j]  #, 'is a(n)' 
    
    for i in range(j+1, len(names)):
        print '\n', 'this is the  ', j, 'outer loop'
        print names[j], 'and', names[i]
        print '\n'
         
        

#for name in names:
#    print name