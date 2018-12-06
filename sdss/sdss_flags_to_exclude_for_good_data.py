import pickle

file_name = 'SdssFlagsDict.sav'
flags_file = open(file_name, 'r')
FlagsDict = pickle.load(flags_file)
flags_file.close()

# print int(FlagsDict["BLENDED"], 0)
# print int(FlagsDict["NOPROFILE"], 0)
# print int(FlagsDict["BRIGHT"], 0)
# print int(FlagsDict["SATURATED"], 0)
# print int(FlagsDict["PEAKCENTER"], 0)
# print int(FlagsDict["DEBLEND_NOPEAK"], 0)
# print int(FlagsDict["NOTCHECKED"], 0)
# print int(FlagsDict["TOO_FEW_GOOD_DETECTIONS"], 0)

my_flag_list = [int(FlagsDict["BLENDED"], 0),int(FlagsDict["NOPROFILE"], 0),int(FlagsDict["BRIGHT"], 0),int(FlagsDict["SATURATED"], 0),int(FlagsDict["PEAKCENTER"], 0),int(FlagsDict["DEBLEND_NOPEAK"], 0),int(FlagsDict["NOTCHECKED"], 0),int(FlagsDict["TOO_FEW_GOOD_DETECTIONS"], 0)]

print my_flag_list




