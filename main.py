#!/usr/bin/env python3

"""
Étude 05 - A Patchwork Quilt
Author(s): Nathan Hardy
"""

import math
import sys
from PIL import Image

# Target size for the image we produce
_TARGET_SIZE = 1024

def main():
    """
    Main Program Logic
    """

    squares = []

    # Read in lines from stdin and construct a list of tuples
    # for the squares, where the tuple is (scale, red, green, blue)
    for unstripped_line in sys.stdin.readlines():
        line = unstripped_line.strip()
        s, *colours = line.split()
        scale = float(s)
        red, green, blue = map(int, colours)
        squares.append((scale, red, green, blue))

    # Calculate the furthest scale distance from the centre point
    max_distance = sum(map(lambda s: s[0] / 2, squares))
    # Given the maximum scale distance, calculate a number of pixels
    # per scale unit, such that the squares fill up the available space
    pixels_per_unit = math.floor((_TARGET_SIZE / 2) / max_distance)

    # Create a new Python Image Library Image instance, with white background
    image = Image.new('RGB', (_TARGET_SIZE, _TARGET_SIZE), 'white')
    pixels = image.load()

    # Instantiate a list of square centres
    centres = [(_TARGET_SIZE // 2, _TARGET_SIZE // 2)]
    for scale, r, g, b in squares:
        # Get the side length for these squares
        length = math.floor(scale * pixels_per_unit)
        # For the next set of squares, create a new list of centres
        new_centres = []

        # For each of the square centres:
        for cx, cy in centres:
            x1 = cx - length // 2
            y1 = cy - length // 2
            x2 = cx + length // 2
            y2 = cy + length // 2

            # The next set of squares will include the squares centred
            # at the corner of this square
            new_centres += [(x1, y1), (x2, y1), (x1, y2), (x2, y2)]

            for y in range(y1, y2):
                for x in range(x1, x2):
                    # Set the colour value for this pixels
                    pixels[x, y] = (r, g, b)

        # Replace the list of centres with the new one
        centres = new_centres

    # Output raw BMP data to stdout
    # Note: Using sys.stdout.buffer instead of sys.stdout
    # because of stdout buffering for large outputs
    image.save(sys.stdout.buffer, 'BMP')

if __name__ == '__main__':
    main()
