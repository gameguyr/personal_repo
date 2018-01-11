#! /usr/bin/python2.7

#Purpose
# To handle calculations done with electrons
# in Quantum Mechanics
# all in  MKS Units!!


import numpy as np

e = 1.60217733E-19
me = 9.109389E-31
mp = 1.672623E-27
mn = 1.674927E-27
h = 6.626075E-34
h_bar = 6.626075E-34/float(2*np.pi)
e_o = 8.854187817E-12
k = (1/(4*np.pi*e_o))
ev_per_joule = 6.24150934E18
a_o = 5.29177249E-11
c = 2.99792458E8

def energy(charge, mass, Z, n):
    binding_energy = -mass*charge**4 *Z**2/float(8*e_o**2*h**2*n**2)
    return binding_energy*ev_per_joule

def energy_int(charge, mass, Z, n):
    binding_energy = -mass*charge**4 *Z**2/float(8*e_o**2*h**2*n**2)
    interaction_energy = (1/float(4*np.pi*e_o))*charge**2/float(a_o)
    return (binding_energy+interaction_energy)*ev_per_joule


