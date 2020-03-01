"""Python Julia set generator for the twitter account FractalDiary.

by : Chittaro Hugo
"""

# Import
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from datetime import date
import logging
import time
from palettable.scientific.diverging import Vik_20

# Execution time
start_time = time.time()

# Var
today = date.today()

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


def main(xmin=-2,
         xmax=2,
         ymin=-2,
         ymax=2,
         wResolution=1000,
         hResolution=1000,
         dpi=100,
         max_iter=100,
         cmap='hot'):
    """Render the Julia set.

    :param xmin: limit of the image.
    :param xmax: limit of the image.
    :param ymin: limit of the image.
    :param ymax: limit of the image.
    :param wResolution: number of pixel in wide (resolution).
    :param hResolution: number of pixel in wide (resolution).
    :param dpi: density of pixel.
    :param max_iter: maximum iteration per point.
    :param cmap: color used for the rendering.
    :return: Image of the Julia set
    :rtype: png image
    """
    logging.info('Started rendering Julia set')

    r1 = np.linspace(xmin, xmax, wResolution, dtype=np.float32)
    r2 = np.linspace(ymin, ymax, hResolution, dtype=np.float32)
    z = r1 + r2[:, None]*1j
    n3 = julia(x, y, z, max_iter)
    n3 = n3.astype(float)

    plt.figure(dpi=dpi)
    plt.imsave("Exports/export-"+str(today)+".png",
                                            n3.T,
                                            cmap=cmap)
    logging.info('Executed in {} seconds, export name : export-{}.png'
                 .format(time.time() - start_time, str(today)))


main(cmap=Vik_20)
