#!/Users/rlego/anaconda/bin/python
# trying to solve some sample programming questions
#  this one is with recursion

def exponent(x, y):
    if y == 0:
        return 1
    elif y<0:
        return 1/(x*exponent(x, abs(y)-1))
    else:
        return x*exponent(x, y-1)


if __name__ == '__main__':
	print exponent(2, -3)