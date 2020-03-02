import numpy as np
import matplotlib.pylab as pl
import matplotlib.colors as clr


def Colormap(*colors):
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
    n = 1000
    x = np.linspace(0, 1, 100)
    y = 0*x + 1
    test = Colormap('#000000', '#FF0000', '#000000')(np.linspace(0, 1, n))
    for i in range(n):
        pl.plot(x, i*y, color=test[i])
    pl.show()
