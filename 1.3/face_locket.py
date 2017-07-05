#/usr/bin/python3

'''When running in ipython, use 'ipython --pylab' for an interactive shell that is matplotlib aware, and/or set matplotlib.pyplot.ion()'''

import numpy as np
from scipy import misc
import pylab as plt
import matplotlib

matplotlib.pyplot.ion()

face = misc.face(gray=True)

sy, sx = face.shape
y,x = np.ogrid[0:sy, 0:sx]
y.shape, x.shape

centerx, centery = (660, 300)
mask = ((y - centery)**2/200**2 + (x - centerx)**2/300**2) > 1 

face[mask]=0
plt.imshow(face)

