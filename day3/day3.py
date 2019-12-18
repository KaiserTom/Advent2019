import math
import sys
import os
import ast

def shift_right(x, y, shift):
    return x + shift, y

def shift_left(x, y, shift):
    return x - shift, y

def shift_up(x, y, shift):
    return x, y + shift

def shift_down(x, y, shift):
    return x, y - shift


def load_inputs():
    linevectors = {}
    with open("day3input.txt", "r") as file:
        for line, linemoves in enumerate(file):
            li = list(linemoves.split(","))
            linevectors[line] = li

    return linevectors

def line_drawer(linevectors):
    x, y, shift, totalsteps = 0, 0, 0, 0
    switch = {
        "R" : shift_right,
        "L" : shift_left,
        "U" : shift_up,
        "D" : shift_down
    }

    line1coords = [[0, 0, 1000000]]
    for vector in linevectors[0]:
        direction = vector[0]
        shift = int(vector[1:4])
        x, y = switch[direction](x, y, shift)
        totalsteps = totalsteps + shift
        coord = [x, y, totalsteps]
        line1coords.append(coord)

    x, y, totalsteps = 0, 0, 0
    line2coords = [[0, 0, 1000000]]
    for vector in linevectors[1]:
        direction = vector[0]
        shift = int(vector[1:4])
        x, y = switch[direction](x, y, shift)
        totalsteps = totalsteps + shift
        coord = [x, y, totalsteps]
        line2coords.append(coord)

    return line1coords, line2coords

def find_linecross(line1coords, line2coords):
    intersects = []
    totalsteps = 0
    for index1, line1coord1 in enumerate(line1coords):
        if (index1 + 1 >= len(line1coords)):
            break

        line1coord2 = line1coords[index1 + 1]
        x1, x2 = line1coord1[0], line1coord2[0]
        y1, y2 = line1coord1[1], line1coord2[1]

        for index2, line2coord1 in enumerate(line2coords):
            if (index2 + 1 >= len(line2coords)):
                break

            line2coord2 = line2coords[index2 + 1]
            x3, x4 = line2coord1[0], line2coord2[0]
            y3, y4 = line2coord1[1], line2coord2[1]

            if (max(x1, x2) < min(x3, x4) or min(x1, x2) > max(x3, x4) or
                max(y1, y2) < min(y3, y4) or min(y1, y2) > max(y3, y4)):
                continue
            
            if(x1 == x2):
                totalsteps = (line1coord1[2] + abs(y3 - y1)) + (line2coord1[2] + abs(x1 - x3))
                intersect = [x1, y3, totalsteps]
            else:
                totalsteps = (line1coord1[2] + abs(x3 - x1)) + (line2coord1[2] + abs(y1 - y3))
                intersect = [x3, y1, totalsteps]

            if(intersect[0] == 0 and intersect[1] == 0):
                continue

            intersects.append(intersect)
    
    while True:
        try:
            intersects.remove([0, 0])
        except:
            break

    return intersects
            
def find_closestintersect(intersects):
    mindistance = 1000000
    for intersect in intersects:
        distance = intersect[2]
        #distance = abs(intersect[0]) + abs(intersect[1])
        if distance < mindistance:
            mindistance = distance

    
    return mindistance

#first key is the line, second key is the movement, third key is the character within the movement
linevectors = load_inputs()
line1coords, line2coords = line_drawer(linevectors)
print(line1coords[0:5])
print(line2coords[0:5])
intersects = find_linecross(line1coords, line2coords)
print(intersects)
mindistance = find_closestintersect(intersects)
print(mindistance)


#print(linevectors[0][2][1:4])
#print(linevectors[1][2][1:4])