#!/usr/bin/python
########################
# TITLE: secret_santa
# AUTHOR: russell lego
# DATE: 2018-12-14
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import numpy

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################

class SecretSanta(object):

    # number_of_participants = len(participants)
    def __init__(self):
        self.MINIMUM_NUMBER_OF_PARTICIPANTS = 4
        self.participants = []
        self.santa_array_of_arrays= []

    def add_participant(self, name_string):
        # self.participants = []
        self.participants.append(name_string)

    def add_participant_with_name_string_array(self, name_string_array):
        for name in name_string_array:
            self.add_participant(name)

    def delete_participants(self):
        self.participants = []

    def delete_santa_array_of_arrays(self):
        self.santa_array_of_arrays = []

    def add_pair_to_santa_array_of_arrays(self, pair_array):
        self.santa_array_of_arrays.append(pair_array)

    def assign_santa_for_participants(self):
        assignment_index_array = numpy.arange(len(self.participants))
        numpy.random.shuffle(assignment_index_array)

        for i in range(0, len(self.participants)):
            temp_array = [self.participants[i], self.participants[assignment_index_array[i]]]
            self.add_pair_to_santa_array_of_arrays(temp_array)

        pairs = self.get_santa_array_of_arrays()

        for i in range(0, len(pairs)):
            # print pairs[i][0], pairs[i][1]
            if pairs[i][0] == pairs[i][1]:
                print '\n'
                print 'Got same santa'
                print '\n'
                print pairs[i][0], pairs[i][1]
                print '\n'
                self.delete_santa_array_of_arrays()
                self.assign_santa_for_participants()


    def get_santa_array_of_arrays(self):
        return self.santa_array_of_arrays





