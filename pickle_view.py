#!/usr/bin/env python

import matplotlib.pyplot as plt
import pickle
from sys import argv

filename = argv[1]

ax = pickle.load( file(filename) )
plt.show()