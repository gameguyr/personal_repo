#! /usr/bin/python2.7

def any_func(r):
    '''takes a number or an array and gives the output'''
    
    return 50/float((r)**(3/2.0)+1)


if __name__=="__main__":
    print "the default value is 2"
    print any_func(2)
    