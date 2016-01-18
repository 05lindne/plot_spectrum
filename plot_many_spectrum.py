#!/usr/bin/env python

""" File: plot_many_spectrum.py
	Author: Sarah Lindner
	Date of last change: 18.01.2016

"""
import numpy as np
import matplotlib.pyplot as plt
import pickle # save plots in pickle format which can be opened in interactive window
import argparse
import filename_handling
from matplotlib import colors as col
import matplotlib.cm as cm

# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('in_file', nargs = "+", help = 'input filename(s)')
parser.add_argument('-out', help = 'output filename')
parser.add_argument('-xlimits', nargs = 2, type=int, default=[700, 900],help = 'lower and upper limits for x-axis \n defaults to 700 and 900')
parser.add_argument('-ylimits', nargs = 2, type=int, help = 'lower and upper limits for y-axis')
parser.add_argument('-notitle', action = 'store_true', help = "don't display plot title")
args = parser.parse_args() 


def main():

	print "Reading data from file(s): " +  str( args.in_file )

	# read data
	xdata = []
	ydata = []
	for item in args.in_file:
		in_x, in_y = np.loadtxt( item, delimiter = " ", unpack = True )
		xdata.append( in_x )
		ydata.append( in_y )

	print "...plotting..."

	ax = plt.subplot( 111 )

	cmap = plt.get_cmap("hsv", len(args.in_file))

	for index, ( itemx, itemy ) in enumerate( zip( xdata, ydata ) ):
		plt.plot( itemx, itemy, linestyle = "-", color = cmap(index), marker = '.', markersize = 4 )


	# aestectic cosmetics
	if args.notitle == False:
		plt.title(args.out, fontsize = 23)
	plt.xlabel('Wavelength (nm)', fontsize = 20)
	plt.ylabel('Intensity (a.u.)', fontsize = 20)
	plt.tick_params(axis = 'both', labelsize = 15)

	plt.xlim(args.xlimits[0], args.xlimits[1]) # zoom in on the x-axis
	if (args.ylimits):
		plt.ylim(args.ylimits[0], args.ylimits[1]) # zoom in on the y-axis
	else:
		plt.ylim(0.0, )


	plt.tight_layout() # suppress chopping off labels

	print "... saving figures...."

	plt.savefig( args.out +'.pdf' )
	plt.savefig( args.out +'.svg' )
	# plt.savefig( ( filename_handling.pathname( args.out ) + "/" + args.out +'.pdf'))
	pickle.dump(ax, file( ( args.out +'.pickle' ), 'w') )
	# pickle.dump(ax, file(( filename_handling.pathname( args.out ) + "/" + args.out +'.pickle'), 'w'))

	plt.show()

	print "...done."

if __name__ == '__main__':
    main()