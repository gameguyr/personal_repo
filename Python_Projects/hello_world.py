#!/usr/bin/python

print "Hello World!"
s="I am tired"
print s[:-2]

for i,x in enumerate([1,2,5,7]):
	print("List{0} = {1}".format(i,x))

print "format" in dir("some string")

print (range (1,10))
print list(range(1,10))
print (3 in range(1,10))

print list(range(1,10)) is [1,2,3,4,5,6,7,8,9]

def somefunc():
    print "I'm in somefunc!"

d = {"blah":somefunc()}

d["blah"]

g = lambda x:x**2

print g(8)
foo = [2,18,9,22,17,24,8,12,27]
""" filter() calls the function for each element in the list and returns a new list
that contains only those elements for which the function returned true.
map() the given function is called for every element in the original list and a new 
list is created which contains the return values from the function
reduce() accepts two arguments, and it operates on two elements from the list
at a time and performs the function on two elements at a time."""
print filter(lambda x:x%3 == 0, foo)
print map(lambda x:x*2 + 10, foo)
print reduce(lambda x, y: x+y, foo)
