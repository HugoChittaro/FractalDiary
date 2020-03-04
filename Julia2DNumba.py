"""Python Julia set generator for the twitter account FractalDiary.

by : Chittaro Hugo
"""

# Imports
from numba import jit, guvectorize, complex64, int32, float32
import numpy as np
import matplotlib.pyplot as plt
from random import uniform
from datetime import date
import logging
import time

# Execution time
start_time = time.time()

# Var
today = date.today()

message = """Julia set | {}\n
Resolution : {} x {} ;
Iteration : {} ;
Colormap : {} ;
c = {} + {}i
#Mathematics #Fractals #Raspberrypi #Python"""

# Random number
x = uniform(-1.25, -0.75)
y = uniform(-0.25, 0.25)


@jit(int32(float32, float32, complex64, int32))
def julia(x, y, z, maxiter):
    """Calculate the escape time for each point on the grid.

    :param x: random value for c on real axis
    :param y: random value for c on imaginary axis
    :param z: a point of the grid
    :param maxiter: maximum iteration before considering that the point escape
    :return: Escape time for each points
    :rtype: int
    """
    c = complex(-0.8, 0.156)
    nreal = 0
    real = z.real
    imag = z.imag
    for n in range(maxiter):
        nreal = real*real - imag*imag + c.real
        imag = 2 * real * imag + c.imag
        real = nreal
        if real * real + imag * imag > 4.0:
            return n
    return 0  # Change to maxiter to change style


@guvectorize([(complex64[:],
             int32[:],
             int32[:])],
             '(n),()->(n)',
             target='parallel')
def julia_numpy(z, maxit, output):
    """Use the mandelbrot fonction on each point of the grid.

    :param z: a point of the grid
    :param maxit: maximum iteration before considering that the point escape
    :return: None, "gufunc kernel must have void return type"(guvectorize)
    :rtype:
    """
    maxiter = maxit[0]
    for i in range(z.shape[0]):
        output[i] = julia(x, y, z[i], maxiter)


def julia_set(xmin=-2,
              xmax=2,
              ymin=-2,
              ymax=2,
              width=1000,
              height=1000,
              dpi=300,
              maxiter=100,
              cmap='hot'):
    """Render the Julia set.

    :param xmin: limit of the image.
    :param xmax: limit of the image.
    :param ymin: limit of the image.
    :param ymax: limit of the image.
    :param wResolution: number of pixel in wide (resolution).
    :param hResolution: number of pixel in wide (resolution).
    :param dpi: density of pixel.
    :param maxiter: maximum iteration per point.
    :param cmap: color used for the rendering.
    :return: Message to be uploaded
    :rtype: string
    """
    logging.info('Started rendering Julia set')

    r1 = np.linspace(xmin, xmax, width, dtype=np.float32)
    r2 = np.linspace(ymin, ymax, height, dtype=np.float32)
    z = r1 + r2[:, None]*1j
    n3 = julia_numpy(z, maxiter)

    logging.info('Julia set rendered in {} seconds'
                 .format(time.time() - start_time))

    plt.figure(dpi=dpi)
    plt.imsave('Exports/export-'+str(today)+'.png',
                                            n3.T,
                                            cmap=cmap)
    logging.info('Executed in {} seconds | export : export-{}.png'
                 .format(time.time() - start_time,
                         str(today),
                         str(height),
                         str(width),
                         str(maxiter)))

    return message.format(str(today),
                          str(height),
                          str(width),
                          str(maxiter),
                          str(cmap),
                          str(x),
                          str(y))


# Test
if __name__ == "__main__":

    # Logging config
    logging.basicConfig(filename='log',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    julia_set(width=1000, height=1000)
    print('Executed in {} seconds'.format(time.time() - start_time))
