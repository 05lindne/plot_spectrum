#!/usr/bin/env python

""" File: plot_spectrum.py
	Author: Sarah Lindner
	Date of last change: 13.11.2015

"""
import numpy as np
import matplotlib.pyplot as plt
import pickle # save plots in pickle format which can be opened in interactive window
import argparse
import filename_handling

# get arguments from command line
parser = argparse.ArgumentParser()
parser.add_argument('in_file', help = 'input filename')
parser.add_argument('-xlimits', nargs = 2, type=int, default=[700, 900],help = 'lower and upper limits for x-axis \n defaults to 700 and 900')
parser.add_argument('-ylimits', nargs = 2, type=int, help = 'lower and upper limits for y-axis')
parser.add_argument('-notitle', action = 'store_true', help = "don't display plot title")
args = parser.parse_args() 


def main():

	print "Plotting file: %r" % args.in_file

	my_filestub = filename_handling.filestub( args.in_file )

	xdata, ydata = np.loadtxt( args.in_file, delimiter=" ", unpack=True) # read data



	ax = plt.subplot(111)

	plt.plot(xdata, ydata, linestyle = "-", color = 'black', marker = '.', markersize=4)


	# aestectic cosmetics
	if args.notitle == False:
		plt.title(my_filestub, fontsize = 23)
	plt.xlabel('Wavelength (nm)', fontsize = 20)
	plt.ylabel('Intensity (a.u.)', fontsize = 20)
	plt.tick_params(axis = 'both', labelsize = 15)

	plt.xlim(args.xlimits[0], args.xlimits[1]) # zoom in on the x-axis
	if (args.ylimits):
		plt.ylim(args.ylimits[0], args.ylimits[1]) # zoom in on the y-axis

	plt.tight_layout() # suppress chopping off labels



	plt.savefig( ( filename_handling.pathname( args.in_file ) + "/" + my_filestub +'.pdf'))
	pickle.dump(ax, file(( filename_handling.pathname( args.in_file ) + "/" + my_filestub +'.pickle'), 'w'))

	# plt.show()



if __name__ == '__main__':
    main()