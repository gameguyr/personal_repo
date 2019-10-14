#!/usr/bin/python
########################
# TITLE: working_with_matplotlib_patches
# AUTHOR: russell lego
# DATE: 2019-10-14
# PURPOSE: to use the circle patch object
########################


#################################
# Importing Modules
#################################
import matplotlib.pyplot as plt

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################
def create_circle():
    circle = plt.Circle((0, 0), radius=5)
    return circle

def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis("scaled")
    plt.show()



#################################
# Defining Classes
#################################


#################################
# Performing Work
#################################

if __name__ == "__main__":
    c = create_circle()
    show_shape(c)