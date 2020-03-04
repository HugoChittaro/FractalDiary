"""Python Julia set generator for the twitter account FractalDiary.

by : Chittaro Hugo
"""
import numpy as np
import matplotlib.pylab as pl
import matplotlib.colors as clr


def colorMapCustomDist(**colors):
    """Create custom colormap with a custom repartition of color.

    :**color: anchor color for colorsmaps
    :return: A color map
    :rtype: matplotlib color map
    """
    buff = []

    for key in colors.keys():
        buff.append((colors[key], key))
    cmap = clr.LinearSegmentedColormap.from_list('custom cmap',
                                                 buff,
                                                 N=256)
    return cmap


def colorMap(*colors):
    """Create custom colormap.

    :*color: anchor color for colorsmaps
    :return: A color map
    :rtype: matplotlib color map
    """
    buff = []
    dist = np.linspace(0, 1, len(colors))
    for index, el in enumerate(colors):
        buff.append((dist[index], el))
    cmap = clr.LinearSegmentedColormap.from_list('custom cmap',
                                                 buff,
                                                 N=256)
    return cmap


if __name__ == "__main__":
    anchor = {'#000764': 0,
              '#206bcb': 0.16,
              '#edffff': 0.42,
              '#ffaa00': 0.6425,
              '#000200': 0.8575,
              '#000765': 1}
    n = 1000
    x = np.linspace(0, 1, 100)
    y = 0*x + 1
    test = colorMapCustomDist(**anchor)(np.linspace(0, 1, n))
    for i in range(n):
        pl.plot(x, i*y, color=test[i])
    pl.show()
