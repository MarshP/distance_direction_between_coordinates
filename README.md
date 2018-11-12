### How to use ###

Download x_y_distance_calc.py and run_x_y_distance_calc.py to the same folder/directory. `python run_x_y_distance_calc.py`

### What it does now ###

Put in two sets of Minecraft or real world map coordinates. The script will give you back the distance and direction between them. The script is aware of the Y-axis difference between real-worls and Minecraft maps.

### Gotchas ###

You're inputting coordinates, you need to know the scale to get a sensible use of the output. This is easy in Minecraft since 1 point of difference == 1m. Harder in an Ordnance Survey map.

There's no input checking. Use numbers or get an error.

### To-Do ###

* Add input checking and error handling
* Add an option to input scale (as distance between coordinates) and give absolute distance in the output
