#!/usr/bin/env python
"""
A test case for the default week 3 assignment. Running this as a program
with your assignment called pdb_stats.py should let you know

The following functions need to be defined:
    * validate_pdbid(pdbid)
    * build_url(pdbid)
    * download_pdb(pdbid)
    * pdb_lines(pdb_data)
    * is_atom_line(line)
    * is_title_line(line)
    * parse_atom_line(line)
    * atom_x_pos(atom)
    * atom_y_pos(atom)
    * atom_z_pos(atom)
    * atom_element(atom)
    * atom_residue(atom)
    * update_range(old_range, num)
    * volume(x_range, y_range, z_range)
    * bounding_box(x_range,y_range,z_range)
    * parse_pdb(pdb_lines)
    * pdb_title(pdb)
    * pdb_bounding_box_corners(pdb)
    * pdb_bounding_box_volume(pdb)
    * pdb_atom_count(pdb)
"""

from __future__ import print_function   # Use print()instead of built-in
from __future__ import unicode_literals # Allow fancy characters by default
from __future__ import division         # Division uses floating point

import gzip
import os
import random
import sys
import unittest

from functools import reduce
from math import sqrt
from operator import __mul__ as mul

try:
    from requests import get as download
except:
    download = None

try:
    unicode = unicode
except:
    def unicode(string):
        return str(string, "utf-8")

try:
    import pdb_stats
except ImportError as e:
    print("Could not locate your assignment file.")
    print("Please make sure the file is named 'pdb_stats.py' and located")
    print("in the directory: {0}.".format(os.path.dirname(__file__)))
    sys.exit(-1)

def open_pdb(path):
    """
    Opens a PDB file on the system and returns :class:list of the file's lines.
    Since many PDBs come gzip compressed, this will attempt to decompress if
    the path name ends with ".gz"

    :param code: PDB ID to create URL to
    :raise OSError: If an error occurred while opening the file
    :return: The a generator of the lines of the PDB file
    """
    base, ext = os.path.splitext(path)
    open_method = gzip.open if ext == ".gz" else open

    with open_method(path) as pdb:
        return pdb.read()

def get_stats(pdb):        
    lines = pdb_stats.pdb_lines(pdb)
    return pdb_stats.parse_pdb(lines)

def render_pdb_stats(pdb):
    output  = ""
    output += "Name: {0}\n".format(pdb_stats.pdb_title(pdb))
    output += "Total Atoms: {0}\n".format(pdb_stats.pdb_num_atoms(pdb))
    output += "Atom Counts:\n"
    for count in pdb_stats.pdb_atom_count(pdb):
        output += "\t{0}: {1}\n".format(*count)
    output += "Bounding Box:\n"
    output += "\tVolume: {0}\n".format(pdb_stats.pdb_bounding_box_volume(pdb))
    output += "\tCorners:\n"
    for point in pdb_stats.pdb_bounding_box_corners(pdb):
        output += "\t\t{0}\n".format(point)
    return output

class PdbTestCase(unittest.TestCase):

    REQUIRED = [
        "validate_pdbid",
        "build_url",
        "download_pdb",
        "pdb_lines",
        "is_atom_line",
        "is_title_line",
        "parse_atom_line",
        "atom_x_pos",
        "atom_y_pos",
        "atom_z_pos",
        "atom_element",
        "atom_residue",
        "update_range",
        "volume",
        "bounding_box",
        "parse_pdb",
        "pdb_title",
        "pdb_bounding_box_corners",
        "pdb_bounding_box_volume",
        "pdb_num_atoms",
    ]

    TEST_PDB_FILE = "test.pdb"
    TEST_PDB_ID = "1erb"
    TEST_PDB_HEADER = "HEADER    RETINOL TRANSPORT"
    # This is only the first title line. That is all we will be checking
    TEST_PDB_TITLE = "The Interaction Of N-Ethyl Retinamide With Plasma Retinol-"
    TEST_PDB_ATOMS = 1401
    TEST_PDB_VOLUME = 81358.2472219
    TEST_PDB_CORNERS = [(50.617, 47.76, 24.185),
                    	(50.617, 47.76, 65.182),
                		(3.107, 47.76, 65.182),
                		(3.107, 5.99, 65.182),
                		(3.107, 47.76, 24.185),
                		(50.617, 5.99, 24.185),
                		(3.107, 5.99, 24.185),
                		(50.617, 5.99, 65.182)]

    TEST_TITLE = "CRYSTAL STRUCTURE OF XANTHINE DEHYDROGENASE ISOLATED FROM BOVINE MILK"
    TEST_LINES = [
        'HEADER    OXIDOREDUCTASE                          24-AUG-00   1FO4              ',
        'TITLE     CRYSTAL STRUCTURE OF XANTHINE DEHYDROGENASE ISOLATED FROM BOVINE MILK ',
        'ATOM    301  CE  LYS A  40      48.787  33.372  23.962  1.00 20.38           C  ',
        'ATOM    302  NZ  LYS A  40      48.934  31.990  24.478  1.00 20.14           N  ',
        'ATOM    303  N   LEU A  41      44.307  37.282  26.604  1.00 19.81           N  ',
        'ATOM    304  CA  LEU A  41      43.648  38.408  27.248  1.00 19.56           C  ',
        'ATOM    305  C   LEU A  41      44.770  39.420  27.419  1.00 19.60           C  ',
        'ATOM    306  O   LEU A  41      45.754  39.142  28.108  1.00 18.90           O  ',
        'ATOM    307  CB  LEU A  41      43.101  38.032  28.637  1.00 19.97           C  ',
        'HETATM22185  O   HOH B4800      67.540 -31.566  66.642  1.00 54.75           O  ',
        'CONECT  32020140                                                                ']

    X_POS = [48.787, 48.934, 44.307, 43.648, 44.770, 45.754, 43.101]
    Y_POS = [33.372, 31.990, 37.282, 38.408, 39.420, 39.142, 38.032]
    Z_POS = [23.962, 24.478, 26.604, 27.248, 27.419, 28.108, 28.637]

    X_RANGE = (43.101, 48.934)
    Y_RANGE = (31.990, 39.420)
    Z_RANGE = (23.962, 28.637)

    BOUNDING_BOX = [(43.101, 31.99, 23.962), 
                    (43.101, 31.99, 28.637), 
                    (43.101, 39.42, 23.962), 
                    (43.101, 39.42, 28.637), 
                    (48.934, 31.99, 23.962), 
                    (48.934, 31.99, 28.637), 
                    (48.934, 39.42, 23.962), 
                    (48.934, 39.42, 28.637)]

    ELEMENT = ['C', 'N', 'N', 'C', 'C', 'O', 'C']
    RESIDUE = ['LYS', 'LYS', 'LEU', 'LEU', 'LEU', 'LEU', 'LEU']

    def setUp(self):
        self._defined = dir(pdb_stats)
        self._missing = list(set(PdbTestCase.REQUIRED) - set(self._defined))
        TEST_LINES = PdbTestCase.TEST_LINES
        self._atom_lines = TEST_LINES[2:9]
        self._title_line = TEST_LINES[1]
        self._ignore_lines = TEST_LINES[0:1] + TEST_LINES[9:]
        self._test_pdb = "\n".join(TEST_LINES)

        try:
            self._parsed_atoms = []
            for line in self._atom_lines:
                self._parsed_atoms.append(pdb_stats.parse_atom_line(line))        
        except:
            self._parsed_atoms = None
        
        try:
            self._parsed_pdb = pdb_stats.parse_pdb(TEST_LINES)
        except:
            self._parsed_pdb = None
    
        try:
            self._downloaded_pdb = download(PdbTestCase.TEST_PDBID)
        except:
            self._downloaded_pdb = None
    
    def skip_if_missing(self, name):
        if name in self._missing:
            self.skipTest("Function '{0}' not found pdb_stats".format(name))

    def skip_if_no_requests_package(self):
        if download is None:
            self.skipTest("Package 'requests' not found. Skipping download tests")
    
    def check_full_pdb(self, pdb):
        self.check_title(PdbTestCase.TEST_PDB_TITLE, 
                         pdb_stats.pdb_title(pdb))
        self.assertEqual(PdbTestCase.TEST_PDB_ATOMS, 
                         pdb_stats.pdb_num_atoms(pdb))
        self.check_within_epsilon(PdbTestCase.TEST_PDB_VOLUME, 
                                  pdb_stats.pdb_bounding_box_volume(pdb))
        self.check_bounding_box_rounding(PdbTestCase.TEST_PDB_CORNERS,
                                         pdb_stats.pdb_bounding_box_corners(pdb))

    def check_title(self, expected, actual):
        # Ignore anything that goes beyond the expected value
        if len(actual) > len(expected):
            actual = actual[:len(expected)]

        self.assertEqual(expected.lower(), actual.lower())
        self.assertEqual(expected, actual, "Title Caps not equal (use str.title())")

    def check_bounding_box_epsilon(self, expected_ranges, actual, eps=.1):
        x, y, z = expected_ranges
        for point in actual:
            px, py, pz = point
            self.assertTrue(((1+eps) * max(x) >= px >= (1-eps) * min(x))
                        and ((1+eps) * max(y) >= py >= (1-eps) * min(y))
                        and ((1+eps) * max(z) >= pz >= (1-eps) * min(z)))

    def check_bounding_box_rounding(self, expected, actual, places=0):
        # This is intentionally weird and obfuscated. Do not use this method.
        # If you understand it, congrats!
        # set . map $ (tuple . map $ round) 
        to_places = lambda x: round(x, places)
        rounded = lambda pts: set(map(lambda p: tuple(map(to_places, p)), pts))
        self.assertEqual(rounded(expected), rounded(actual))

    def check_range_volume_epsilon(self, expected_ranges, actual, eps=.05):
        # This is intentionally weird and obfuscated. Do not use this method.
        # If you understand it, congrats!
        x, y, z = expected_ranges
        expected = reduce(mul, map(lambda u: sqrt((max(u)-min(u))**2), (x,y,z)))
        self.check_within_epsilon(expected, actual, eps)
    
    def check_within_epsilon(self, expected, actual, eps=.05):
        self.assertTrue((1+eps) * expected >= actual >= (1-eps) * expected)

    def test_00_missing_functions(self):
        self.assertEqual(list(self._missing), [])

    def test_01_validate_pdbid(self):
        self.skip_if_missing('validate_pdbid')

        self.assertTrue(pdb_stats.validate_pdbid("1fo4"))
        self.assertFalse(pdb_stats.validate_pdbid("|fo4"))
        self.assertFalse(pdb_stats.validate_pdbid("1ffo44"))

    def test_02_pdb_lines(self):
        self.skip_if_missing('pdb_lines')

        self.assertEqual(pdb_stats.pdb_lines(self._test_pdb), PdbTestCase.TEST_LINES)

    def test_03_is_atom_line(self):
        self.skip_if_missing('is_atom_line')

        for line in self._atom_lines:
            self.assertTrue(pdb_stats.is_atom_line(line))
        for line in self._ignore_lines:
            self.assertFalse(pdb_stats.is_atom_line(line))
        self.assertFalse(pdb_stats.is_atom_line(self._title_line))

    def test_04_is_title_line(self):
        self.skip_if_missing('is_title_line')

        self.assertTrue(pdb_stats.is_title_line(self._title_line))
        for line in self._atom_lines:
            self.assertFalse(pdb_stats.is_title_line(line))
        for line in self._ignore_lines:
            self.assertFalse(pdb_stats.is_title_line(line))

    def test_05_parse_atom_line(self):
        self.skip_if_missing('parse_atom_line')
        
        self._parsed_atoms = []
        for line in self._atom_lines:
            try:
                parsed = pdb_stats.parse_atom_line(line)
                if parsed is not None:
                    self._parsed_atoms.append(parsed)
            except:
                pass

        self.assertEqual(len(self._parsed_atoms), 7)

    def test_06_atom_x_pos(self):
        self.skip_if_missing('atom_x_pos')
        
        if self._parsed_atoms is None:
            self.skipTest("Was unable to parse atom for testing")

        for index, atom in enumerate(self._parsed_atoms):
            expected = PdbTestCase.X_POS[index]
            actual = pdb_stats.atom_x_pos(atom)
            self.assertEqual(round(actual, 1), round(expected, 1))

    def test_07_atom_y_pos(self):
        self.skip_if_missing('atom_y_pos')
        
        if self._parsed_atoms is None:
            self.skipTest("Was unable to parse atom for testing")

        for index, atom in enumerate(self._parsed_atoms):
            expected = PdbTestCase.Y_POS[index]
            actual = pdb_stats.atom_y_pos(atom)
            self.assertEqual(round(actual, 1), round(expected, 1))

    def test_08_atom_z_pos(self):
        self.skip_if_missing('atom_z_pos')
        
        if self._parsed_atoms is None:
            self.skipTest("Was unable to parse atom for testing")

        for index, atom in enumerate(self._parsed_atoms):
            expected = PdbTestCase.Z_POS[index]
            actual = pdb_stats.atom_z_pos(atom)
            self.assertEqual(round(actual, 1), round(expected, 1))
    
    def test_09_atom_element(self):
        self.skip_if_missing('atom_element')
        
        if self._parsed_atoms is None:
            self.skipTest("Was unable to parse atom for testing")

        for index, atom in enumerate(self._parsed_atoms):
            expected = PdbTestCase.ELEMENT[index]
            actual = pdb_stats.atom_element(atom)
            self.assertEqual(expected, actual)

    def test_10_atom_residue(self):
        self.skip_if_missing('atom_residue')
        
        if self._parsed_atoms is None:
            self.skipTest("Was unable to parse atom for testing")

        for index, atom in enumerate(self._parsed_atoms):
            expected = PdbTestCase.RESIDUE[index]
            actual = pdb_stats.atom_residue(atom)
            self.assertEqual(expected, actual)

    def test_11_update_range(self):
        self.skip_if_missing('update_range')
        
        test = (1,10)
        self.assertEqual(test, (1,10))
        self.assertEqual(pdb_stats.update_range(test, 0),  (0,10))
        self.assertEqual(pdb_stats.update_range(test, 11), (1,11))
        self.assertEqual(pdb_stats.update_range(test, 5),  (1,10))
        self.assertEqual(pdb_stats.update_range(test, -1), (-1,10))
        self.assertEqual(pdb_stats.update_range(test, 90), (1,90))

    def test_12_volume(self):
        self.skip_if_missing('volume')
        
        self.assertEqual(pdb_stats.volume((0,1), (2,3), (4,5)), 1)
        self.assertEqual(pdb_stats.volume((5,10), (25,30), (100,105)), 125)

        x = PdbTestCase.X_RANGE
        y = PdbTestCase.Y_RANGE
        z = PdbTestCase.Z_RANGE
        eps = .05
        
        point_ranges = (x, y, z)
        actual = pdb_stats.volume(*point_ranges)
        self.check_range_volume_epsilon(point_ranges, actual)

    def test_13_bounding_box(self):
        self.skip_if_missing('bounding_box')
    
        expected = set([(0,0,0),(0,0,1),(0,1,0),(0,1,1),
                        (1,0,0),(1,0,1),(1,1,0),(1,1,1)])
        actual = set(pdb_stats.bounding_box((0,1),(0,1),(0,1)))
        self.assertEqual(actual, expected)

        x = PdbTestCase.X_RANGE
        y = PdbTestCase.Y_RANGE
        z = PdbTestCase.Z_RANGE
        point_ranges = (x, y, z)
        actual = list(pdb_stats.bounding_box(*point_ranges))

        self.check_bounding_box_epsilon(point_ranges, actual)
        self.check_bounding_box_rounding(PdbTestCase.BOUNDING_BOX, actual)

    def test_14_parse_pdb(self):
        self.skip_if_missing('parse_pdb')

        self.assertTrue(pdb_stats.parse_pdb(PdbTestCase.TEST_LINES))

    def test_15_pdb_title(self):
        self.skip_if_missing('pdb_title')

        if self._parsed_pdb is None:
            self.skipTest("Was unable to parse PDB for testing")
        
        expected = PdbTestCase.TEST_TITLE.title()
        actual = pdb_stats.pdb_title(self._parsed_pdb)

        self.check_title(expected, actual)

    def test_16_pdb_bounding_box_corners(self):
        self.skip_if_missing('pdb_bounding_box_corners')

        if self._parsed_pdb is None:
            self.skipTest("Was unable to parse PDB for testing")

        x = PdbTestCase.X_RANGE
        y = PdbTestCase.Y_RANGE
        z = PdbTestCase.Z_RANGE
        point_ranges = (x, y, z)
        actual = list(pdb_stats.pdb_bounding_box_corners(self._parsed_pdb))
        self.check_bounding_box_epsilon(point_ranges, actual)
        self.check_bounding_box_rounding(PdbTestCase.BOUNDING_BOX, actual)

    def test_17_pdb_bounding_box_volume(self):
        self.skip_if_missing('pdb_bounding_box_volume')

        if self._parsed_pdb is None:
            self.skipTest("Was unable to parse PDB for testing")

        x = PdbTestCase.X_RANGE
        y = PdbTestCase.Y_RANGE
        z = PdbTestCase.Z_RANGE
        point_ranges = (x, y, z)
        actual = pdb_stats.pdb_bounding_box_volume(self._parsed_pdb)
        self.check_range_volume_epsilon(point_ranges, actual)

    def test_18_pdb_atom_count(self):
        self.skip_if_missing('pdb_num_atoms')

        if self._parsed_pdb is None:
            self.skipTest("Was unable to parse PDB for testing")

        actual = pdb_stats.pdb_num_atoms(self._parsed_pdb)
        expected = len(PdbTestCase.ELEMENT)
        self.assertEqual(expected, actual)

    def test_19_build_url(self):
        self.skip_if_missing('build_url')
        
        self.assertIsNone(pdb_stats.build_url("This should be None"))
        
        url = pdb_stats.build_url(PdbTestCase.TEST_PDB_ID)
        try:
            # This is a hack for 2-3 compatibility
            result = unicode(download(url).content) 
            self.assertTrue(result.startswith(PdbTestCase.TEST_PDB_HEADER))
        except:
            self.skipTest("Download was unable to complete")
    
    def test_20_download_pdb(self):
        self.skip_if_no_requests_package()
        self.skip_if_missing('download_pdb')

        downloaded = unicode(pdb_stats.download_pdb(PdbTestCase.TEST_PDB_ID))
        self.assertTrue(downloaded.startswith(PdbTestCase.TEST_PDB_HEADER))

    def test_21_full_pdb_from_file(self):
        if len(self._missing) > 0:
            self.skipTest("Cannot run full test without all functions defined")
        
        if not os.path.exists(PdbTestCase.TEST_PDB_FILE):
            self.skipTest("Cannot find {0} to run test".format(PdbTestCase.TEST_PDB_FILE))

        pdb = open_pdb(PdbTestCase.TEST_PDB_FILE)
        stats = get_stats(pdb)
        self.check_full_pdb(stats)

    def test_22_full_pdb_from_internet(self):
        self.skip_if_no_requests_package()

        if len(self._missing) > 0:
            self.skipTest("Cannot run full test without all functions defined")

        pdb = unicode(pdb_stats.download_pdb(PdbTestCase.TEST_PDB_ID))
        stats = get_stats(pdb)
        self.check_full_pdb(stats)

def arg_to_test_name(arg, tests):
    if arg.isdigit():
        possible = [t for t in tests if t.startswith("test_{0:02d}_".format(int(arg)))]
    else:
        possible = [t for t in tests if t.endswith(arg)]
    return possible[0] if len(possible) > 0 else None

def run(args):
    """
    This will initiate a test of your pdb_stats program
    """
    if len(args) > 1:
        possible_tests = [fn for fn in dir(PdbTestCase) if fn.startswith("test_")]
        requested_tests = [arg_to_test_name(test, possible_tests) for test in args[1:]]
        valid_tests = [test for test in requested_tests if test is not None]
        test_names = ["test_case.PdbTestCase.{0}".format(t) for t in valid_tests]
        suite = unittest.TestLoader().loadTestsFromNames(test_names)
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(PdbTestCase)
    return unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    # No argparse just because
    if len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']:
        print("Usage: python test_case.py [test_name,]")
        print()
        print("Will test assignment 2 for CSC206")
        print("With no additional arguments, all tests will be run")
        print("Valid test names are:")
        col_width = max(map(len, PdbTestCase.REQUIRED)) + 5
        for num,test in enumerate(PdbTestCase.REQUIRED):
            endl = "\n" if (num+1) % 3 == 0 and num > 0 else ""
            print("({}) ".format(num).rjust(5), end="")
            print(test.ljust(col_width), end=endl)
        print()
        sys.exit()
    results = run(sys.argv)
    sys.exit()
    if len(results.errors) == 0 \
   and len(results.failures) == 0 \
   and os.path.exists(PdbTestCase.TEST_PDB_FILE):
        pdb = open_pdb(PdbTestCase.TEST_PDB_FILE)
        stats = get_stats(pdb)
        print("Rendered Output")
        print(render_pdb_stats(stats))
