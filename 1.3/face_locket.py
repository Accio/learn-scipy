#/usr/bin/python3

import numpy as np
from scipy import misc
import pylab as plt

face = misc.face(gray=True)
plt.show(face)

sy, sx = face.shape
y,x = np.ogrid[0:sy, 0:sx]
y.shape, x.shape

centerx, centery = (660, 300)
mask = ((y - centery)**2 + (x - centerx)**2) > 230**2

face[mask]=0
plt.show(face)

