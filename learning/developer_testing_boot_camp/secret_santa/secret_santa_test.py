#!/usr/bin/python
########################
# TITLE: secret_santa_test
# AUTHOR: russell lego
# DATE: 2018-12-14
# PURPOSE:
########################


#################################
# Importing Modules
#################################
import unittest
import secret_santa
#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################
class SecretSantaTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(SecretSantaTest, self).__init__(*args, **kwargs)
        self.secret_santa_class = secret_santa.SecretSanta()

    # def test_more_than_three_participants(self):
    #
    #     secret_santa_class = secret_santa.SecretSanta()

    def test_a_participant_can_be_added(self):
        self.secret_santa_class.add_participant('Amy')
        self.assertEqual(len(self.secret_santa_class.participants), 1)

    def test_is_true_for_unique_array_of_names(self):
        self.secret_santa_class.delete_participants()
        participants = ['Harry', 'Sally', 'Memnon', 'Mamose', 'Lostris']
        self.secret_santa_class.add_participant_with_name_string_array(participants)
        self.assertEqual(len(list(set(self.secret_santa_class.participants))), len(self.secret_santa_class.participants))

    def test_is_false_for_non_unique_array_of_names(self):
        self.secret_santa_class.delete_participants()
        participants = ['Harry', 'Sally', 'Memnon', 'Mamose', 'Mamose']
        self.secret_santa_class.add_participant_with_name_string_array(participants)
        self.assertFalse(len(list(set(self.secret_santa_class.participants))) == len(self.secret_santa_class.participants))


    def test_is_true_for_minimum_number_of_participants(self):
        self.secret_santa_class.delete_participants()
        participants = ['Harry', 'Sally', 'Memnon', 'Mamose', 'Lostris']
        self.secret_santa_class.add_participant_with_name_string_array(participants)

        self.assertTrue(len(self.secret_santa_class.participants) >= self.secret_santa_class.MINIMUM_NUMBER_OF_PARTICIPANTS)

    def test_is_true_for_no_self_santa(self):
        self.secret_santa_class.delete_participants()
        participants = ['Harry', 'Sally', 'Memnon', 'Mamose', 'Lostris']
        self.secret_santa_class.add_participant_with_name_string_array(participants)
        self.secret_santa_class.assign_santa_for_participants()
        pairs = self.secret_santa_class.get_santa_array_of_arrays()

        for i in range(0, len(pairs)):
            # print pairs[i][0], pairs[i][1]
            self.assertTrue(pairs[i][0] != pairs[i][1])

        print "Final List", pairs


#################################
# Performing Work
#################################

