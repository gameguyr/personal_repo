#!/usr/bin/python
########################
# TITLE: two sum
# AUTHOR: russell lego
# DATE: 2018-07-27
# PURPOSE:
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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_array = []
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    index_array.append(i)
                    index_array.append(j)
                    return index_array


#################################
# Performing Work
#################################
if __name__ == "__main__":
    solution = Solution()
    input_nums = [-1, 16, 8, 11, 15]
    input_target = 10
    my_solution = solution.twoSum(input_nums, input_target)
    print my_solution