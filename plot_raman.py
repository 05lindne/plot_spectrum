#!/usr/bin/env python

""" File: plot_raman.py
	Author: Sarah Lindner
	Date of last change: 11.01.2016
"""

import matplotlib.pyplot as plt
import numpy as np
import math
import os
import pickle # save plots in pickle format which can be opened in interactive window

import argparse
import filename_handling

# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('in_file', help = 'input filename')
parser.add_argument('-xlimits', nargs = 2, type=int, default=[600, 2000],help = 'lower and upper limits for x-axis \n defaults to 600 and 2000')
parser.add_argument('-ylimits', nargs = 2, type=int, help = 'lower and upper limits for y-axis')
parser.add_argument('-notitle', action = 'store_true', help = "don't display plot title")
args = parser.parse_args() 

def main():


	print "Plotting file: %r" % args.in_file

	my_filestub = filename_handling.filestub( args.in_file )

	ax = plt.subplot(111)
	

	wavelength, luminescence = np.loadtxt( args.in_file, delimiter=" ", unpack=True) # read data

	wavenumber = convert_wavelength_wavenumber( wavelength, 532.0 )

	my_dataplot = plt.plot( wavenumber, luminescence, marker = '.', markersize=4, 
		linestyle = "-", color = 'black', label="Measurement" )

	if args.notitle == False:
		plt.title(my_filestub , fontsize = 23)
	plt.xlabel(r'Raman Shift (cm$^{-1}$)', fontsize = 20)
	plt.ylabel('Intensity (a.u.)', fontsize = 20)
	plt.tick_params(axis = 'both', labelsize = 15)

	plt.xlim(args.xlimits[0], args.xlimits[1]) # zoom in on the x-axis
	if (args.ylimits):
		plt.ylim(args.ylimits[0], args.ylimits[1]) # zoom in on the y-axis
	plt.tight_layout()


	plt.savefig( ( filename_handling.pathname( args.in_file ) + "/" + my_filestub +'.pdf'))
	plt.savefig( ( filename_handling.pathname( args.in_file ) + "/" + my_filestub +'.svg'))
	pickle.dump(ax, file(( filename_handling.pathname( args.in_file ) + "/" + my_filestub +'.pickle'), 'w'))

	# show()



def convert_wavelength_wavenumber( wavelength, excitation ):
	wavenumber_all = []
	for item in wavelength:
		wavenumber = ( 1 / (excitation*10**(-9)) )   -   ( 1 / (item*10**(-9)) )
		wavenumber_all.append( wavenumber/(10**2) )
	return wavenumber_all

if __name__ == '__main__':
    main()