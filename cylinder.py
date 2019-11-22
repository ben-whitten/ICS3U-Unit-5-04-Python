#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which finds the volume of the cylinder.

import math


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def calculations(height_copy, radius_copy):
    # This does the calculations
    area = (math.pi*(radius_copy**2)*height_copy)
    return area


def main():
    # This is what gets the dimensions of the cylinder
    while True:
        radius_as_string = input(color.YELLOW + 'Input the radius of the' +
                                 ' cylinder: ' + color.END)
        height_as_string = input(color.YELLOW + "Input the height" +
                                 " of the cylinder: " + color.END)

        try:
            radius = int(radius_as_string)
            height = int(height_as_string)
            
            if radius >= 0 and height >= 0:
                area = calculations(radius_copy=radius, height_copy=height)
                print("{0}cm^3".format(area))
                break

            else:
                print('')
                print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                      ' number...' + color.END)
                print("")
                print("")

        except Exception:
            print('')
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")


if __name__ == "__main__":
    main()
