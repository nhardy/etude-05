#!/usr/bin/env python3

"""
Étude 05 - A Patchwork Quilt
Author(s): Nathan Hardy
"""

import math
import sys

class Bitmap:
    """
    Bitmap writer
    """

    def __init__(self, dimensions: tuple, background: tuple = (255, 255, 255)):
        self.width, self.height = dimensions
        self._pixels = [[background for cell in range(self.width)] for row in range(self.height)]

    def set_pixel(self, coords: tuple, colour: tuple):
        x, y = coords
        r, g, b = colour
        self._pixels[y][x] = (r, g, b)

    def binary(self): bytearray:
        bmp_size = b'\x00\x00\x00\x00' # TODO: this
        reserved = b'\x00\x00\x00\x00'
        offset = b'\x00\x00\x00\x00' # TODO: this
        return b'BM' + bmp_size + reserved + offset + b''

_TARGET_SIZE = 20

def main():
    squares = []

    for unstripped_line in sys.stdin.readlines():
        line = unstripped_line.strip()
        s, *colours = line.split()
        scale = float(s)
        red, green, blue = map(int, colours)
        squares.append((scale, red, green, blue))

    max_distance = sum(map(lambda s: s[0] / 2, squares))
    pixels_per_unit = math.floor((_TARGET_SIZE / 2) / max_distance)

    image = Bitmap((_TARGET_SIZE, _TARGET_SIZE))
    image.set_pixel((0, 0), (0, 0, 0))

    print(pixels_per_unit)

if __name__ == '__main__':
    main()
