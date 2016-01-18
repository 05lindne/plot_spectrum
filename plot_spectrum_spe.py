#!/usr/bin/env python

""" File: plot_spectrum.py
	Author: Sarah Lindner
	Date of last change: 21.05.2015

	Takes filesname of .SPE file as input.
"""
import sys
sys.path.append('/mnt/Daten/my_programs/plot/')

import pylab as plt
from sys import argv
import os
import pickle # save plots in pickle format which can be opened in interactive window
from python_misc_modules import winspec # module which can handle winspec .SPE files 
										# visit https://github.com/kaseyrussell/python_misc_modules to download package
										# and http://people.seas.harvard.edu/~krussell/html-tutorial/index.html for documentation

import filename_handling # custom functions for working with filenames & directories


def main():


	# argv is your commandline arguments, argv[0] is your program name, so skip it
	my_file = argv[1]
	if len(argv) > 2:
		xlim_lower = float( argv[2] )
		xlim_upper = float( argv[3] )


	print "Plotting file: %r" % my_file


	my_filestub = filename_handling.filestub( my_file )

	ax = plt.subplot(111)

	my_spectrum = winspec.Spectrum( my_file )


	my_dataplot = my_spectrum.plot( marker = '.', markersize=4, 
		linestyle = "-", color = 'black', label="Measurement" )

	title_file_name = my_filestub.replace('spe_', '')

	plt.title( title_file_name , fontsize = 23)
	plt.xlabel('Wavelength (nm)', fontsize = 23)
	plt.ylabel('Intensity (a.u.)', fontsize = 23)
	plt.tick_params(axis = 'both', labelsize = 23)
	if 'xlim_lower' in locals() and 'xlim_upper' in locals():
		plt.xlim(xlim_lower, xlim_upper) # zoom in on the x-axis
	plt.tight_layout()

	axes = plt.gca()
	axes.set_xlim([min(xdata),max(xdata)])

	if ( filename_handling.extension( my_file ) == 'SPE'):
		print 'Saving .txt file'
		wavelength, luminescence = winspec.get_spectrum(my_file)
		plt.savetxt(filename_handling.pathname(my_file) + "/" + my_filestub+'.txt', plt.column_stack((wavelength, luminescence)))


	plt.savefig( ( filename_handling.pathname(my_file) + "/" + my_filestub +'.pdf'))
	pickle.dump(ax, file((filename_handling.pathname(my_file) + "/" + my_filestub +'.pickle'), 'w'))

	# plt.show()



if __name__ == '__main__':
    main()