#! /usr/bin/python2.7

#####################
# PURPOSE: To choose a random workout so I can exercise
#
# DATE: 
#
# AUTHOR: Russell Lego
####################


from PIL import Image
from random import randrange


path = '/Users/lego/git/personal_repo/ActivityImages'

picture_dictionary={'swim': 'swim.png',
                    'bike': 'bike.png',
                    'run': 'run.png',
                    'hike': 'hike.png',
                    'gym': 'gym.png',
                    'disc': 'disc.png',
                    'elliptical': 'elliptical.png',
                    'yoga':  'yoga.png',
                    'p90x': 'p90x.png'}

print''
print' Are you ready to workout?'
print''

decision = raw_input('Please enter y/n:   ')
if decision == 'y':
    number = randrange(len(picture_dictionary) - 1)
    workoutImage = Image.open(path +'/' + picture_dictionary[picture_dictionary.keys()[number]])
    workoutImage.show()
else:
    print ''
    print 'Well come back when you are ready!!'
    print''
                           