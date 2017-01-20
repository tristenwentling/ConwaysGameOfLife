from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

def graph_show(grid):
    """shows a graphical version of the board"""
    side = len(grid)
    image = Image.new('RGB',(side*3, side*3))
    #  pix_dead = (000, 000, 000)  # black
    #  pix_live = (073, 172, 057)  # green
    pix_dead = (255, 255, 255)  # white
    pix_live = (000, 000, 000)  # black
    for i in range(side):
        for j in range(side):
            tup = grid[i][j][0]
            a = i * 3
            b = a + 1
            c = b + 1
            d = j * 3
            e = d + 1
            f = e + 1
            if tup == 1:
                image.putpixel((a, d), pix_live)
                image.putpixel((b, e), pix_live)
                image.putpixel((c, f), pix_live)
            else:
                image.putpixel((a, d), pix_dead)
                image.putpixel((b, e), pix_dead)
                image.putpixel((c, f), pix_dead)
    image.save("newimage2.gif")
    image.show()
