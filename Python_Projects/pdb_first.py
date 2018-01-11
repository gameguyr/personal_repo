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
  pdb = str(f.text)
  newline = ""	 
  pdb_file = []
  for line in pdb:
    if line != '\n':
      newline = newline + line
    else:
      pdb_file.append(newline)
      newline = ""
  if (f.status_code == 200):
      return pdb_file
  else:
    print "Unable to obtain pdb file for PDBID: %s." % (str(pdbid))
    sys.exit("Exiting program")

"""Takes a string containing the contents of a PDB file and returns a list containing the TITLE in the first element and a list of atoms in the second element."""
def pdb_lines(pdb_data):
  atoms = []
  header = ""
  title = []
  newline = ""
  for line in pdb_data:
    if(is_title_line(line)):
       newline = str(line)
       title.append(newline)
    elif(is_header_line(line)):
       newline = str(line)
       newline.strip()
       header = header + newline
    elif(is_atom_line(line)):
       atom = parse_atom_line(line)
       atoms.append(atom)
    elif(is_terminal_line(line)):
       break
  pdb_file = [title,atoms,header]
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
  length = y_range[1] - y_range[0]
  width = x_range[1] - x_range[0]
  height = z_range[1] - z_range[0]
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
  title_list = pdb_lines[0]
  header = pdb_lines[2]
  atoms = pdb_lines[1]
  title = pdb_title(title_list)
  PDBid = pdb_id(header)
  num_atoms = pdb_atom_count(atoms)
  amino_acids = pdb_residue(atoms)		
  box = pdb_bounding_box_corners(atoms)
  volume = pdb_bounding_box_volume(box)
  elements = pdb_elements(atoms)
  return [title,PDBid,num_atoms,amino_acids,box,volume,elements]

"""Returns the name (title) of the PDB file."""
def pdb_title(pdb):
  title = ""
  for x in pdb:
    temp = x[5:81]
    x = temp.strip()
    title = title + " " + x
  title.strip()  
  return title

"""Returns the original PDB ID supplied."""
def pdb_id(pdb):
  return pdb[62:66] 

"""The set of (x,y,z) points defining the PDB bounding box."""
def pdb_bounding_box_corners(pdb):
  x_range = [0,0]
  y_range = [0,0]
  z_range = [0,0]
  for atom in pdb:
     temp = atom[0]
     x = float(temp)
     y = float(atom[1])
     z = float(atom[2])
     x_range = update_range(x_range,x)
     y_range = update_range(y_range,y)
     z_range = update_range(z_range,z)
  box = bounding_box(x_range,y_range,z_range)
  return box

"""Returns a float representing the volume of the bounding box around all of the atoms in the PDB file. 
  The parameter "pdb" is actually the box_coordinates, because I didn't see the need to go through all the
  atoms again to find the range"""
def pdb_bounding_box_volume(pdb):
  minimum = pdb[0]
  maximum = pdb[6]
  x_range = [minimum[0],maximum[0]]
  y_range = [minimum[1],maximum[1]]
  z_range = [minimum[2],maximum[2]]
  box_volume = volume(x_range, y_range, z_range)
  return box_volume

"""Returns the total number of atoms in the PDB file."""
def pdb_atom_count(pdb):
  return len(pdb)

"""Returns a dictionary containing all the residues as the key and their values are the number of 
occurences for each residue seen in this protein."""
def pdb_residue(pdb):
  residues = dict()
  for x in pdb:
    if residues.has_key(x[3]):
      residues[x[3]] +=1
    else:
      residues[x[3]] = 1
  return residues

"""Returns a dictionary containing all the elements as the key and their values are the number of 
occurences for each element seen in this protein."""
def pdb_elements(pdb):
  elements = dict()
  for x in pdb:
    if elements.has_key(x[4]):
      elements[x[4]] += 1
    else:
      elements[x[4]] = 1
  return elements
  
"""The stats parameter is a list with the following format: stats = [title,pbid,num_atoms,amino_acids,box,volume,elements].
It prints all of the data along with their corresponding statistics. """
def print_statistics(stats):
  print "\nThe title for the PDB id %s is the following:" % str(stats[1])
  print stats[0]
  print "\nThe number of atoms in this protein is %d \n" % stats[2]
  print "The following is a picture of a box with corners labled A-F\n to identify the box coordinates more easily:\n "
  print_bounding_box()
  letter = 65
  box = stats[4]
  for x in box:
    print (chr(letter) + ": ")
    print x
    letter = letter + 1
  print "\nThe volume of the box is: %f \n" % (stats[5])
  print "The following are the amino_acids seen in this protein, \nalong with the number of occurences: \n"
  residue = stats[3]
  for x in residue:
     print x + ": " + str(residue[x])
  print "\nThe following are the elements seen in this protein,\n along with the number of occurences: \n"
  elements = stats[6]
  for x in elements:
     print x + ": " + str(elements[x])

if __name__ == "__main__":
  id = raw_input("Please enter a PDB id: ")
  pdb_file = download_pdb(id)
  pdb_list = pdb_lines(pdb_file)
  stats = parse_pdb(pdb_list)
  print_statistics(stats)

