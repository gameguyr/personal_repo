(int(f['DEBLEND_NOPEAK'], 0) + int(f['TOO_FEW_GOOD_DETECTIONS'], 0)) & flags[0] == int(f['TOO_FEW_GOOD_DETECTIONS'], 0)





int(f['BINNED1'], 0) & flags[0] > 0  and  int(f['TOO_FEW_GOOD_DETECTIONS'], 0) & flags[0] > 0 and int(f['DEBLEND_NOPEAK'], 0) & flags[0] > 0

for flag in BadFlags:
    if not(flag == 'NOTCHECKED'):
        print 'not(int(FlagsDict["'+flag+'"], 0) & CatData["flags"] > 0 ) and \\'
    else:
        print 'not(int(FlagsDict["'+flag+'"], 0) & CatData["flags"] > 0 )'
    
##   WORKS !!!##
index1 = (int(FlagsDict["BLENDED"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["NOPROFILE"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["BRIGHT"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["SATURATED"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["PEAKCENTER"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["DEBLEND_NOPEAK"], 0) & CatData['flags'] == 0)  & \
(int(FlagsDict["NOTCHECKED"], 0) & CatData['flags'] == 0) & \
(int(FlagsDict["TOO_FEW_GOOD_DETECTIONS"], 0) & CatData['flags'] == 0) 


i1=(int(FlagsDict["BLENDED"], 0) & CatData['flags'] == 0)
i2=(int(FlagsDict["NOPROFILE"], 0) & CatData['flags'] == 0)

