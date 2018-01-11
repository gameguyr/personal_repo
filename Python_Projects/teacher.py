"""
polynomials.py

sample program for Math  400

bic 1/31/13
    2/2/13   revised

* represent a polynomial by a list
* show examples of functions that print the polynomial
* take the derivative of a polynomial
* start exploring a different list representation of a polynomial

"""

testP = [1,0,1,7,0,4]



def printPoly1(P):
    for i in range(len(P)):
        print("%s x^%s + "%(P[i], i)),
    print

def printPoly2(P):
    for i in range(len(P)):
        if P[i] != 0:
            print("%s x^%s + "%(P[i], i)),
    print

def reverse(L):
    R = []
    for i in range(len(L)-1,-1,-1):
        R.append(L[i])
    return(R)

def printPoly3(P):
    for i in reverse(range(len(P))):
        if P[i] != 0:
            print("%s x^%s + "%(P[i], i)),
    print

def printPoly4(P):
    for i in reverse(range(len(P))):
        if P[i] != 0:
            if i != 0:
                print("%s x^%s + "%(P[i], i)),
            else:
                print("%s"%(P[i])),
    print

def derivative(P):
    "returns dP/dx"
    D=[]
    for i in range(1,len(P)):
        D.append(P[i]*i)
    return(D)


def test(P,v=4):
    if v>0:
        print("printPoly1(testP) returns:")
        printPoly1(P)
    if v>1:
        print("printPoly2(testP) returns:")
        printPoly2(P)
    if v>2:
        print("printPoly3(testP) returns:")
        printPoly3(P)
    if v>3:
        print("printPoly4(testP) returns:")
        printPoly4(P)


def testDerivative(P):
    print("Derivatives:")
    printPoly4(P)
    for i in range(len(P)):
        P = derivative(P)
        printPoly4(P)



#######
# second representation

testP2 = [[4,5],[7,3],[1,1],[1,0]]


def printPPoly1(P):
    for i in range(len(P)):
        print("%d x^%s + "%(P[i][0], P[i][1])),
    print

def testPPoly(P):
    print("printPPoly1(%s) is:"%(P))
    printPPoly1(testP2)

#######

test(testP)
testDerivative(testP)

testPPoly(testP2)
