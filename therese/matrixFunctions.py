#!/usr/bin/python

"""

matrixFunctions.py

2/5/13  bic

This is a skeleton for the matrix part of first Math 400 assignment

"""

#######  START Administrivia 
m400group = 1   # change this to your group number

m400names = ['Ola Gold', 'Therese Demers', 'Shujia Zhang','Nathan Bauer','Yi-Hsien Chen'] # change this for your names

def printNames():
    print("matrixFunctions.py for group %s:"%(m400group)),
    for name in m400names:
        print("%s, "%(name)),
    print

printNames()

#######  END Administrivia

def showMatrix(mat):
    "Print out matrix"
    for row in mat:
        print(row)


def zeroMatrix(m,n):
    "Create zero matrix"
    new_mat = []
    zero_row = []
    for col in range(n):
        zero_row.append(0)
    for row in range(m):
        new_mat.append(zero_row)
    return(new_mat)
 

def rows(mat):
    "return number of rows"
    return(len(mat))


def cols(mat):
    "return number of cols"
    return(len(mat[0]))
 

def transpose(mat):
    "return transpose of mat"
    new_mat = [list() for i in xrange(cols(mat))]
    [(new_mat[index].append(item)) for row in mat for index,item in enumerate(row)]
    return new_mat


def getCol(mat, col):
    "return column col from matrix mat"
    column = list()
    [(column.append(row[col])) for row in mat]
    return column


def getRow(mat, row):
    "return row row from matrix mat"
    return mat[row]


def scalarMultMatrix(a,mat):
    "multiply a scalar times a matrix"
    new_mat = [list() for i in xrange(cols(mat))]
    [(new_mat[index].append(item*a)) for index,row in enumerate(mat) for i,item in enumerate(row)]
    return(new_mat)


def addMatrices(A,B):
    "add two matrices"
    if cols(A) is not cols(B):
      return 0
    new_mat = [list() for i in xrange(rows(A))]
    temp_mat = zip(A,B)
    temp_mat = [zip(rowA,rowB)for rowA,rowB in temp_mat]
    [new_mat[index].append(x+y) for index,data in enumerate(temp_mat) for x,y in data]
    return(new_mat)


def multiplyMat(A,B):
    "multiply two matrices"
    if cols(A) != rows(B) or cols(B) != rows(A):
      return 0
    new_mat = [list() for i in xrange(cols(B))]
    for index,row in enumerate(A):
        for x,y in enumerate(B):
          columnMat = getCol(B,x)
          temp_row = zip(row,columnMat)
          temp_row = [reduce(lambda i,j: i*j, pair) for pair in temp_row] 
          temp_row = reduce(lambda i,j: i+j, temp_row) 
          new_mat[index].append(temp_row)
    return(new_mat)

def printMatrix(A):
    for index,row in enumerate(A):
      print row

if __name__=="__main__":

    A = [[4,-2,1,11],
        [-2,4,-2,-16],
        [1,-2,4,17]]

    Ae = [[4,-2,1],
         [-2,4,-2],
         [1,-2,4]]
   
    D = [[1,2,3],
        [4,5,6],
        [7,8,9]]

    B = [11,-16,17]

    C = [2,3,5]

    print("running matrixFunction.py file")
    
    print "Transposing matrix: "
    printMatrix(D)
    N = transpose(D)
    print "Transposed matrix: "
    printMatrix(N)
    print "Second column matrix in transposed matrix: " 
    col = getCol(N,1)
    printMatrix(col)
    print "Second row matrix in transposed matrix: " 
    row = getRow(N,1)
    print(row)
    print "Multiplying the scalar 2 to the original matrix (before transposing): "
    mmat = scalarMultMatrix(2,D)
    printMatrix(mmat)
    print "Adding and multiplying the following two matrices: "
    print "Matrix 1: "
    printMatrix(D)
    print "Matrix 2: "
    printMatrix(Ae)    
    F = addMatrices(D,Ae)
    G = multiplyMat(D,Ae)
    print "The resulting matrix from adding them: "
    printMatrix(F)
    print "The resulting matrix from multiplying them: "
    printMatrix(G)
