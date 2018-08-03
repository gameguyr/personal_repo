#!/usr/bin/python
########################
# TITLE: reverse_integer
# AUTHOR: russell lego
# DATE: 2018-08-02
# PURPOSE: Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
########################


#################################
# Importing Modules
#################################


#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################
class Solution(object):
    def reverse_integer(self, x):
        """

        :param x:
        :return:
        """

        if x > 2**31 or x < -2**31:
            return 0

        my_list = list(str(x))
        is_negative = False

        if my_list[0] == '-':
            is_negative = True
            my_negative = my_list.pop(0)

        my_list.reverse()
        tmp_string = ''
        for i in range(0, len(my_list)):
            tmp_string = tmp_string + my_list[i]

        my_reversed_int = int(tmp_string)

        if is_negative:
            my_reversed_int = -1 * my_reversed_int

        return my_reversed_int




#################################
# Performing Work
#################################

if __name__ == '__main__':
    solution = Solution()
    input = -9349073456
    answer = solution.reverse_integer(input)
    print answer

