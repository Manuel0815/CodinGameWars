import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append({'distance': distance, 'duration': duration})

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

# s = v * t
valid = False
while not valid:
    valid = True
    for light in lights:
        arrival_time = light['distance'] / (speed/3.6)
        if int(round(arrival_time /  light['duration'], 10)) % 2 != 0:
            valid = False
            speed -= 1
            break

print(str(speed))