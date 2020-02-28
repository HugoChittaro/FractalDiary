"""Python Julia set generator for the twitter account FractakWeather.

by : Chittaro Hugo
"""

# Import
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from datetime import date

# Option
# c = -0.7654 + 0.2020j
max_iter = 100
cmap = 'hot'
interpolation = 'bilinear'

# Windows
w = 1000
h = 1000
dpi = 100
xmin = -2
xmax = 2
ymin = -2
ymax = 2

# Var
result = np.zeros([h, w])

# Random number
x = uniform(-1.25, -0.75)
y = uniform(-0.25, 0.25)


def julia(x, y, z, max_iter):
    """Calculate the escape time for each (x;y) points.

    :param x: real part of complex number
    :param y: imaginary part of complex number
    :param max_iter: maximum iteration before getting to the next point.
    :return: Julia set
    :rtype: array
    """
    output = np.zeros(z.shape, np.complex64)
    c = np.zeros(z.shape, np.complex64)
    c.fill(complex(x, y))
    for it in range(max_iter):
        notdone = np.less(z.real*z.real + z.imag*z.imag, 4.0)
        output[notdone] = it
        z[notdone] = z[notdone]**2 + c[notdone]
    output[output == max_iter-1] = 0
    return output


r1 = np.linspace(xmin, xmax, w, dtype=np.float32)
r2 = np.linspace(ymin, ymax, h, dtype=np.float32)
z = r1 + r2[:, None]*1j
n3 = julia(x, y, z, max_iter)
result = n3.astype(float)

plt.figure(dpi=dpi)
today = date.today()
plt.imsave("Exports/export-"+str(today)+".png",
                                        result.T,
                                        cmap=cmap)
