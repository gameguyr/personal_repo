#!/usr/bin/python
########################
# TITLE: matrix_multiplcation
# AUTHOR: russell lego
# DATE: 2018-08-20
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

    def matrix_multiply(self, input_matrix_a, input_matrix_b):

        if len(input_matrix_a[0]) == len(input_matrix_b):
            rows_a = len(input_matrix_a)
            cols_a = len(input_matrix_a[0])
            rows_b = len(input_matrix_b)
            cols_b = len(input_matrix_b[0])


            output_matrix = self.matrix_maker(rows_a, cols_b)
            for i in range(0, rows_a):

                for j in range(0, cols_b):
                    temp_sum = 0

                    for k in range(0, cols_a):
                        temp_sum = temp_sum + (input_matrix_a[i][k] * input_matrix_b[k][j])

                    output_matrix[i][j] = temp_sum

            return output_matrix


        else:
            return False

    def matrix_maker(self, number_of_rows, number_of_columns):
        my_matrix = [0] * number_of_rows
        for i in range(0 , number_of_rows):
            my_matrix[i] = [0] * number_of_columns

        return my_matrix


#################################
# Performing Work
#################################

if __name__ == "__main__":
    a = [[1, 2, 1], [3, 6, 9]]
    b = [[8], [4], [2]]
    solution = Solution()

    print solution.matrix_multiply(a, b)