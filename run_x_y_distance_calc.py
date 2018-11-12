# pylint: disable-msg=C0103
# pylint: disable-msg=C0301
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:31:11 2018

@author: Marsh
"""

from x_y_distance_calc import x_y_distance_calc

x_start = int(input(
    "Please enter start location on x or east-west axis. (Use a number without units. All inputs should be in unitless coordinates): "))

y_start = int(input("\nPlease enter start location on y (z in Minecraft) or north-south axis: "))

x_destination = int(input("\nPlease enter destination location on x or east-west axis: "))

y_destination = int(
    input("\nPlease enter destination location on y (z in Minecraft) or north-south axis: "))

print(x_y_distance_calc(x_start, y_start, x_destination, y_destination))

print("Press enter to finish")

raw_input()
