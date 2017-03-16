import math

x_start = int(input("Please enter start location on x or east-west axis.\n\n(Use a number without units. All inputs should be in unitless coordinates): "))
y_start = int(input("\nPlease enter start location on y (z in Minecraft) or north-south axis: "))

x_destination = int(input("\nPlease enter destination location on x or east-west axis: "))
y_destination = int(input("\nPlease enter destination location on y (z in Minecraft) or north-south axis: "))

distance = math.sqrt(((x_destination - x_start)**2)+((y_destination - y_start)**2))
tidy_distance=float("{0:.2f}".format(distance))

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

print('\nDistance decimals is {} (to two d.p), direction is {} {} and {} {}.'.format(tidy_distance, east_west_distance, east_west_direction, north_south_distance, north_south_direction))
print('\nThe result is a number of coordinate-points, which you will convert to distance depending on the scale of your map.')
