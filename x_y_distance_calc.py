# pylint: disable-msg=C0103
# pylint: disable-msg=C0301
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:31:11 2018

@author: Marsh
"""


def x_y_distance_calc(x_start, y_start, x_destination, y_destination):
    import math

    distance = math.sqrt(((x_destination - x_start)**2)+((y_destination - y_start)**2))
    tidy_distance = float("{0:.2f}".format(distance))

    if x_start < x_destination:
        east_west_direction = "east"
    elif x_start == x_destination:
        east_west_direction = "neither east nor west"
    else:
        east_west_direction = "west"

    if y_start < y_destination:
        north_south_direction = "north on a real world map (south in Minecraft)"
    elif y_start == y_destination:
        north_south_direction = "neither north nor south"
    else:
        north_south_direction = "south on a real world map (north in Minecraft)"

    north_south_distance = abs(y_destination - y_start)
    east_west_distance = abs(x_destination - x_start)

    print('\nDistance decimals is {} (to two d.p), direction is {} {} and {} {}.'.format(
        tidy_distance, east_west_distance, east_west_direction, north_south_distance, north_south_direction))
    print('\nThe result is a number of coordinate-points, which you will convert to distance depending on the scale of your map.')
    return tidy_distance
