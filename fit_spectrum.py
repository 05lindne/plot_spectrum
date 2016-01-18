#!/usr/bin/env python

""" File: fit_spectrum.py
	Author: Sarah Lindner
	Date of last change: 26.05.2015

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

	xlim_lower = 700.
	xlim_upper = 900.
	fit_wavelength = 738.
	fit_width = 5.0
	spike_threshold = 50

	# argv is your commandline arguments, argv[0] is your program name, so skip it
	my_file = argv[1]
	if len(argv) > 2:
		xlim_lower = float( argv[2] )
		xlim_upper = float( argv[3] )
	if len(argv) > 4:
		fit_wavelength = float( argv[4] )
		fit_width = float( argv[5] )
	if len(argv) > 6:
		spike_threshold = ( argv[6] )


	print "Fitting file: %r" % my_file

	my_filestub = filename_handling.filestub( my_file )

	fig = plt.figure()
	ax = plt.subplot(111)

	my_spectrum = winspec.Spectrum( my_file)


	fitrange = my_spectrum.get_fitrange_indices((fit_wavelength-fit_width, fit_wavelength+fit_width))

	my_spectrum.fit_lorentzians(
	    center=fit_wavelength,
	    width=fit_width,
	    fitrange=fitrange,
	    number_bestfit_points=1000,
	    plotfit=False  )


	# my_dataplot = my_spectrum.plot( marker = '.', markersize=4, color = 'black', label="Measurement" )
	# fig.canvas.mpl_connect('figure_enter_event', enter_figure)
	# my_spectrum.fit_gaussians(plotfit=False, halfwidth=fit_width, center=fit_wavelength, yoffset=0.0,printparams =True)



	my_spectrum.remove_cosmic_rays(spike_threshold)


	my_dataplot = my_spectrum.plot( marker = '.', markersize=4, color = 'black', label="Measurement" )
	my_fitplot = my_spectrum.plot_fit( '--', linewidth=2.5, color = 'red', label = "Fit") # fit curve lies under data curve

	for peak in my_spectrum.fit_params:
		mywidth = 2*peak['halfwidth']
		mywavelength = peak['x0']



	plt.legend(prop={'size':20})

	title_file_name = my_filestub.replace('spectrum_', '')

	# plt.title('Spectrum to '+title_file_name , fontsize = 23)
	plt.xlabel('Wavelength (nm)', fontsize = 23)
	plt.ylabel('Intensity (a.u.)', fontsize = 23)
	plt.tick_params(axis = 'both', labelsize = 23)
	plt.gca().yaxis.get_major_ticks()[0].set_visible(False) # don't show 
	# plt.gca().yaxis.set_major_locator(MaxNLocator(prune='lower'))
	# my_dataplot, ax = subplots()

	# Show interesting parameters in figure.
	plt.annotate('$\lambda$ = ' + str(round (mywavelength, 2)) + ' nm', fontsize = 23, xy=(0.50, 0.66), xycoords='axes fraction')
	plt.annotate('$\Delta \lambda$ = ' + str(round (mywidth, 2)) + ' nm', fontsize = 23, xy=(0.50, 0.58), xycoords='axes fraction')


	plt.xlim(xlim_lower, xlim_upper) # zoom in on the x-axis
	plt.tight_layout()


	print "Delta lambda : " + str(round (mywidth, 2))


	if ( filename_handling.extension( my_file ) == 'SPE'):
		print 'Saving .txt file'
		wavelength, luminescence = winspec.get_spectrum(my_file)
		plt.savetxt(my_filestub+'.txt', plt.column_stack((wavelength, luminescence)))


	plt.savefig( ( filename_handling.pathname(my_file) + "/" + my_filestub +'_fit.pdf'))
	pickle.dump(ax, file((filename_handling.pathname(my_file) + "/" + my_filestub +'_fit.pickle'), 'w'))

	plt.show()



if __name__ == '__main__':
    main()