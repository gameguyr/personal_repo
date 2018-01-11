#!/Users/rlego/anaconda/bin/python
# trying to solve some sample programming questions
#  this one works

def exponent(x, y):
    if y == 0:
        return 1
    else:
        result=1
        for i in range(1, y+1):
            result=result*x
            
        return result
        