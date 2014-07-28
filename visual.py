from images import Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def graph_show(grid):
    """shows a graphical version of the board"""
    side = len(grid)
    image = Image(side*3, side*3)
    #  pix_dead = (000, 000, 000)  # black
    #  pix_live = (073, 172, 057)  # green
    pix_dead = (255, 255, 255)  # white
    pix_live = (000, 000, 000)  # black
    for i in xrange(side):
        for j in xrange(side):
            tup = grid[i][j][0]
            a = i * 3
            b = a + 1
            c = b + 1
            d = j * 3
            e = d + 1
            f = e + 1
            if tup == 1:
                image.setPixel(a, d, pix_live)
                image.setPixel(b, e, pix_live)
                image.setPixel(c, f, pix_live)
            else:
                image.setPixel(a, d, pix_dead)
                image.setPixel(b, e, pix_dead)
                image.setPixel(c, f, pix_dead)
    image.save("newimage2.gif")
    image.draw()
