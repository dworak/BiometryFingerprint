#lukaszdworakowski

from PIL import Image, ImageDraw
import utils
import argparse
import math
import os

cells = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def minutiae_at(pixels, i, j):
    values = [pixels[i + k][j + l] for k, l in cells]

    crossings = 0
    for k in range(0, 8):
        crossings += abs(values[k] - values[k + 1])
    crossings /= 2

    if pixels[i][j] == 1:
        if crossings == 1:
            return "end"
        if crossings == 3:
            return "y"
    return "none"

def calculate_minutiaes(im):
    pixels = utils.load_image(im)
    utils.apply_to_each_pixel(pixels, lambda x: 0.0 if x > 10 else 1.0)

    (x, y) = im.size
    result = im.convert("RGB")

    draw = ImageDraw.Draw(result)

    colors = {"end" : (150, 0, 0), "y" : (0, 150, 0)}

    ellipse_size = 2
    f = open('output.txt', 'wb+')
    for i in range(1, x - 1):
        for j in range(1, y - 1):
            minutiae = minutiae_at(pixels, i, j)
            if minutiae != "none":
                s = ""
                if minutiae == "end":
                    s = "({0},{1},zakonczenie)\n".format(i,j)
                if minutiae == "y":
                    s = "({0},{1},rozwidlenie)\n".format(i,j)
                f.write(s)
                draw.ellipse([(i - ellipse_size, j - ellipse_size), (i + ellipse_size, j + ellipse_size)], outline = colors[minutiae])

    del draw
    return result
