#!/usr/bin/python
########################
# TITLE: how_to_tell_if_flags are set
# AUTHOR: russell lego
# DATE: 2018-10-10
# PURPOSE: I am trying to remember how to set the flags and
# create an index of objects that do no have certain flags that are set
########################


#################################
# Importing Modules
#################################
import pickle

#################################
# Defining Constants
#################################
# file_name = '/Users/russell.lego/Dropbox/PythonWorkspace/sdss/SdssFlagsDict.sav'
file_name = 'SdssFlagsDict.sav'
flags_file = open(file_name, 'r')
FlagsDict = pickle.load(flags_file)
flags_file.close()

# this is from
# SELECT p.flags
#
# FROM PhotoObj AS p
# WHERE
# p.objid = 1237651226782793869

my_flags_for_test_obj = 35255508930576
integer_representation_of_flag = int(FlagsDict['SUBTRACTED'], 0)


SUBTRACTED = int(FlagsDict['SUBTRACTED'], 0)
INTERP = int(FlagsDict['INTERP'], 0)
ELLIPFAINT = int(FlagsDict['ELLIPFAINT'], 0)


# print my_flags_for_test_obj  & integer_representation_of_flag

print my_flags_for_test_obj  & INTERP

print my_flags_for_test_obj  & ELLIPFAINT

# So i have actually found this excerpt from one of my old pieces of code
#  ##   WORKS !!!##
# index1 = (int(FlagsDict["BLENDED"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["NOPROFILE"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["BRIGHT"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["SATURATED"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["PEAKCENTER"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["DEBLEND_NOPEAK"], 0) & CatData['flags'] == 0)  & \
# (int(FlagsDict["NOTCHECKED"], 0) & CatData['flags'] == 0) & \
# (int(FlagsDict["TOO_FEW_GOOD_DETECTIONS"], 0) & CatData['flags'] == 0)


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

