"""
Author: Therese Demers
File: pdb_stats.py

"""

#!/usr/bin/python 
import re
import requests
import sys

"""Takes a string representation of PDBID and returns true if it's valid. A valid PDBID is defined to be 4 characters long, consisting of #'s and letters."""
def validate_pdbid(pdbid):
  return ((pdbid.isalnum())and(len(pdbid)==4))

"""This takes a PDBID and returns a URL from which to download the PDBID."""
def build_url(pdbid):
  if (validate_pdbid(pdbid) == True):
    return ("http://www.rcsb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId="+str(pdbid))
  else:
    print "PDBID: %s is invalid." % ( str(pdbid))
    sys.exit("Exiting program")

"""Takes a PDBID, downloads it if the id is valid, and returns the contents of the response or none otherwise."""
def download_pdb(pdbid):
  f = requests.get(build_url(pdbid))
  if (f.status_code == 200):
    pdb_file = str(f.text)
    return pdb_file
  else:
    print "Unable to obtain pdb file for PDBID: %s." % (str(pdbid))
    sys.exit("Exiting program")

"""Takes a string containing the contents of a PDB file and returns a list containing the lines of the pdb file """
def pdb_lines(pdb):
  newline = ""	 
  pdb_file = []
  for line in pdb:
    if line != '\n':
      newline = newline + line
    else:
      pdb_file.append(newline)
      newline = ""
  return pdb_file

"""Takes a line from the PDB file and returns true if the line describes an ATOM and returns false otherwise."""
def is_atom_line(line):
  atom = line[:4]
  return (str(atom) == "ATOM")

"""Takes a line from the PDB file and returns true if the line is the title and returns false otherwise."""
def is_title_line(line):
  title = line[:5]
  return (str(title) == "TITLE")

"""Takes a line from the PDB file and returns true if the line is the terminal line; the list of ATOM records for polymer atoms must be terminated by a TER record. (source: http://deposit.rcsb.org/adit/docs/pdb_atom_format.html)"""
def is_terminal_line(line):
  terminal = line[:3]
  return (str(terminal) == "TER")

"""Takes a line from the PDB file and returns true if the line is the HEADER line and returns false otherwise."""
def is_header_line(line):
  header = line[:6]
  return (str(header) == "HEADER")

"""This will take an ATOM line from a PDB file, extracts the x,y,z coordinates, the amino acid/residue and the element of the atom an returns a list representation in the format [x,y,z,residue,element]."""
def parse_atom_line(line):
  x = atom_x_pos(line)
  y = atom_y_pos(line)
  z = atom_z_pos(line)
  residue = atom_residue(line)
  element = atom_element(line)
  atom = [x,y,z,residue,element]
  return atom  

"""Returns the x position of atom as a float."""
def atom_x_pos(atom):
   return float(atom[31:39])

"""Returns the y position of atom as a float."""
def atom_y_pos(atom):
  return float(atom[39:47])

"""Returns the z position of atom as a float."""
def atom_z_pos(atom):
  return float(atom[47:55])

"""Returns a single character string representing the element of the atom (C, S, N, etc.)"""
def atom_element(atom):
  return atom[76:78]

"""Returns a 3 character string representing the residue that the atom is part of."""
def atom_residue(atom):
  return atom[17:20]

"""(old_range is a pair (min, max)) returns a new (min, max) updated with num if necessary."""
def update_range(old_range, num):
  if num < old_range[0]:
    old_range[0] = num
  elif num > old_range[1]:
    old_range[1] = num
  return old_range 

"""Returns a float representing the volume of the box defined by the three ranges."""
def volume(x_range, y_range, z_range):
  length = y_range[1] - y_range[0]  # length = max y value - min y value
  width = x_range[1] - x_range[0]   # width = max x value - min x value
  height = z_range[1] - z_range[0]  # height = max z value - min z value
  return (length*width*height)

"""Returns a list of points defining the corners of the bounding box."""
def bounding_box(x_range,y_range,z_range):
  xmin = x_range[0]
  xmax = x_range[1]
  ymin = y_range[0]
  ymax = y_range[1]
  zmin = z_range[0]
  zmax = z_range[1]

  box_coordinates = [(xmin,ymin,zmin),(xmax,ymin,zmin),(xmax,ymin,zmax),
  (xmin,ymin,zmax),(xmin,ymax,zmin),(xmax,ymax,zmin),(xmax,ymax,zmax),
  (xmin,ymax,zmax)]
  return box_coordinates

"""Prints a bounding box with the points labeled as "A-F" so that when the coordinates of the bounding box are printed, the user can clearly see which set of coordinates pertains to which corner of the box."""
def print_bounding_box():
 print ( "   H********G\n  * *     **\nD********C *\n *  *   *  *\n * E* * *  *F\n * *    * *\nA********B\n")  

"""This takes a list of PDB lines and calculates the final properties of the pdb file."""
def parse_pdb(pdb_lines):
  header = ""
  title = ""
  atoms = []
  residue = dict()
  elements = dict()
  box_range = {'x_range':[0,0], 'y_range':[0,0], 'z_range':[0,0]}
  for line in pdb_lines:
    if(is_title_line(line)):
       newline = str(line)
       temp = newline[5:81]
       temp.strip()
       title = title + " " + temp
    elif(is_header_line(line)):
       newline = str(line)
       header = header + newline
    elif(is_atom_line(line)):
       atom = parse_atom_line(line)
       if residue.has_key(atom[3]):
          residue[atom[3]] += 1
       else:
          residue[atom[3]] = 1
       if elements.has_key(atom[4]):
	  elements[atom[4]] +=1
       else:
          elements[atom[4]] = 1    
       box_range['x_range'] = update_range(box_range['x_range'],float(atom[0]))
       box_range['y_range'] = update_range(box_range['y_range'],float(atom[1]))
       box_range['z_range'] = update_range(box_range['z_range'],float(atom[2]))
       atoms.append(atom)
    elif(is_terminal_line(line)):
       break
  num_atoms = len(atoms)
  box = bounding_box(box_range['x_range'],box_range['y_range'],box_range['z_range'])
  volume = pdb_bounding_box_volume(box)
  stats = {'HEADER': header, 'TITLE': title, 'NUM_ATOMS':num_atoms, 'RESIDUE': residue, 'BOX': box, 'VOLUME': volume, 'ELEMENTS': elements}
  return stats

"""Returns a float representing the volume of the bounding box around all of the atoms in the PDB file.""" 
def pdb_bounding_box_volume(box_corners):
  minimum = box_corners[0]	# [xmin, ymin, zmin]
  maximum = box_corners[6]      # [xmax, ymax, zmax]
  x_range = [minimum[0],maximum[0]]
  y_range = [minimum[1],maximum[1]]
  z_range = [minimum[2],maximum[2]]
  box_volume = volume(x_range, y_range, z_range)
  return box_volume

"""The stats parameter is a dictionary with the following format: stats = {HEADER,TITLE,NUM_ATOMS,RESIDUE,BOX,VOLUME,ELEMENTS}
It prints all of the data along with their corresponding statistics. """
def print_statistics(stats):
  print "\nThe title for this PDB is: %s" % stats['TITLE']
  print "\nThe number of atoms in this protein is %d \n" % stats['NUM_ATOMS']
  print "The following is a picture of a box with corners labled A-F\n to identify the box coordinates more easily:\n "
  print_bounding_box()
  letter = 65
  box = stats['BOX']
  for x in box:
    print (chr(letter) + ": ")
    print x
    letter = letter + 1
  print "\nThe volume of the box is: %f \n" % (stats['VOLUME'])
  print "The following are the amino_acids seen in this protein, \nalong with the number of occurences: \n"
  residue = stats['RESIDUE']
  for x in residue:
     print x + ": " + str(residue[x])
  print "\nThe following are the elements seen in this protein,\n along with the number of occurences: \n"
  elements = stats['ELEMENTS']
  for x in elements:
     print x + ": " + str(elements[x])

if __name__ == "__main__":
  id = raw_input("Please enter a PDB id: ")
  pdb_file = download_pdb(id)
  pdb_list = pdb_lines(pdb_file)
  stats = parse_pdb(pdb_list)
  print_statistics(stats)

