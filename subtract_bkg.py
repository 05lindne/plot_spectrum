#!/usr/bin/env python

""" File: plot_spectrum.py
	Author: Sarah Lindner
	Date of last change: 21.05.2015

	Takes filesname of .SPE file as input.
"""
import sys
sys.path.append('/mnt/Daten/my_programs/plot/')

from sys import argv
import os
import numpy as np

import filename_handling # custom functions for working with filenames & directories

def main():

	in_filename = argv[1]

	xdata, ydata = np.loadtxt( in_filename, usecols=(0, 1), unpack=True)

	# print ydata

	bkg_subtracted_ydata=[]

	for item in ydata:
		bkg_subtracted_ydata.append(item - min(ydata))

	# print bkg_subtracted_ydata

	np.savetxt( (filename_handling.filestub( in_filename ) + '_bkg_subtracted.txt'), np.c_[xdata,bkg_subtracted_ydata])	
	
if __name__ == '__main__':
    main()