#!/usr/bin/python

from __future__ import division

class Stats(Object):
  def mean(grades):
    sum = 0
    for x in grades:
      sum = sum + x
    return sum/len(grades)

  def median(grades):
    if((len(grades))%2 == 0):
      median = (grades[len(grades)//2] + grades[(len(grades)//2)-1])/2
    else:
      median = grades[len(grades)//2]
    return median

  def mode(grades):
    maxCount = 1
    maxNum = []    #maxNum is a list because there could be more than one mode. 
    for x in grades:
      if grades.count(x) >= maxCount:
        if(grades.count(x) == maxCount and maxCount != 1):
          if x in maxNum:
            continue
          else:
            maxNum.append(x)
        elif(grades.count(x) > maxCount):
          del maxNum[:]
          maxNum.append(x)
          maxCount = grades.count(x)
    if(len(maxNum) == 0):
      return "No Mode"
    else:
      return str(maxNum)[1:-1]    #To get rid of the brackets from list  

  def histogram(grades):
    hist = dict()
    for x in grades:
      scoreRange = x//10
      scoreRange = int(scoreRange * 10)
      if hist.has_key(scoreRange):
        hist[scoreRange].append(x)
      else:
        hist[scoreRange] = [x]
    return hist

  def printHistogram(hist):
    print "The following is a histogram for the grades entered: \n"
    startRange = 0
    while(startRange <= 100):
      if startRange not in hist:
        hist[startRange]= []
      startRange = startRange + 10
    hlist = hist.items()
    hlist.sort()
    for r,s in hlist:
      numStars = len(s)
      print "{:>3}: {} ".format(r,'*'*numStars) 

  def main():
    getGrades = True
    grades = []
    while(getGrades == True):
      grade = float(raw_input(" Enter a numerical grade (ie 97.2), or -1 to exit: "))
      end = grade//1
      if(int(end) < 0):
        getGrades = False
      else:
        grades.append(grade)

    grades.sort()
    print "\n Here is a sorted list of the grades you entered:\n"
    print str(grades)[1:-1]
    gradeMean = format(mean(grades), '.3f')
    gradeMedian = median(grades)
    gradeMode = mode(grades)
    print "\nMean: {0}\n".format(gradeMean)
    print "Median: {0}\n".format(gradeMedian)
    print "Mode: {0}\n".format(gradeMode)
    hist = histogram(grades)
    printHistogram(hist)

if __name__ == "__main__":
  main() 
