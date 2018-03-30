import h5py
import numpy as np
import matplotlib.pyplot as plt

filename = '/Users/vskdtc/IdeaProjects/mysql-python/src/s2s.h5'
f = h5py.File(filename, 'r')
print(f.key())