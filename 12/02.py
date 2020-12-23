import string
import os

def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path = os.path.split(full_path)[0]
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
instructions = list(map(lambda x: (x[0:1],int(x[1:])),fileData.splitlines()))

def turn(currentDirection, offSet):
    directions = ['N','E','S','W']
    for i in range(len(directions)):
        if directions[i]==currentDirection:
            return directions[(i+offSet) % len(directions)]

waypoint = [1,10]
coord = [0,0] #+N -S, +E -W
for instruction in instructions:
    travelingDirection = instruction[0]
    distance = instruction[1]

    if (travelingDirection=='R' or travelingDirection=='L'):
        offset = (int(distance/90)*-1)%4
        if travelingDirection=='R':
            offset = (int(distance/90))%4

        if offset==0:
            waypoint = [waypoint[0],waypoint[1]]
        if offset==1:
            waypoint = [waypoint[1]*-1,waypoint[0]]
        if offset==2:
            waypoint = [waypoint[0]*-1,waypoint[1]*-1]
        if offset==3:
            waypoint = [waypoint[1],waypoint[0]*-1]

    if (travelingDirection=='F'):
        coord[0] += waypoint[0]* distance
        coord[1] += waypoint[1]* distance

    if (travelingDirection=='N'):
        waypoint[0] += distance
    if (travelingDirection=='E'):
        waypoint[1] += distance
    if (travelingDirection=='S'):
        waypoint[0] -= distance
    if (travelingDirection=='W'):
        waypoint[1] -= distance

print(coord)
print(str(coord[0]+coord[1]))