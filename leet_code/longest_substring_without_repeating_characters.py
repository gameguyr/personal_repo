#!/usr/bin/python
########################
# TITLE: longest_substring_without_repeating_characters
# AUTHOR: russell lego
# DATE: 2018-07-27
# PURPOSE:Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
########################

#################################
# Defining Classes
#################################
class Solution(object):
    def lengthOfLongestSubstring(self, string):
        """
        :type string: str
        :rtype: int
        """
        temp_longest_string = ''

        for i in range(0, len(string)):
            if i == 0:
                temp_longest_string = string[0]
            for j in range(i+1, len(string)):
                temp_longest_string_2 = string[i:j+1]
                if string[j] not in list(temp_longest_string_2[:-1]):
                    if len(temp_longest_string_2) > len(temp_longest_string):
                        temp_longest_string = temp_longest_string_2
                else:
                    break

        return len(temp_longest_string)




#################################
# Performing Work
#################################

if __name__ == "__main__":
    solution = Solution()
    # input_string = 'barfbarfbarfinyourfaces'
    input_string = "barfbarfbarfinyourface"
    my_solution = solution.lengthOfLongestSubstring(input_string)
    print my_solution