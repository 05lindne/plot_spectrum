#!/usr/bin/env python

""" File: convert_spe.py
	Author: Sarah Lindner
	Date of last change: 13.11.2015

	Takes filesname of .SPE file as input.
"""
import sys
sys.path.append('/mnt/Daten/my_programs/plot/')

import pylab as plt
import os
import argparse
from python_misc_modules import winspec # module which can handle winspec .SPE files 
										# visit https://github.com/kaseyrussell/python_misc_modules to download package
										# and http://people.seas.harvard.edu/~krussell/html-tutorial/index.html for documentation

import filename_handling # custom functions for working with filenames & directories


# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('in_file', help = 'input filename of .SPE file which should be converted to a .txt file')
args = parser.parse_args() 

def main():

	print "Converting spe-file: %r" % args.in_file


	in_filestub = filename_handling.filestub( args.in_file )

	my_spectrum = winspec.Spectrum( args.in_file )

	wavelength, luminescence = winspec.get_spectrum( args.in_file )
	plt.savetxt( filename_handling.pathname( args.in_file ) + "/" + in_filestub +'.txt', plt.column_stack( (wavelength , luminescence ) ) )




if __name__ == '__main__':
    main()