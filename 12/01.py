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

coord = [0,0] #+N -S, +E -W
facingDirection = 'E'
for instruction in instructions:
    travelingDirection = instruction[0]
    distance = instruction[1]

    if (travelingDirection=='R'):
        facingDirection = turn(facingDirection, int(distance/90))
    if (travelingDirection=='L'):
        facingDirection = turn(facingDirection, int(distance/90)*-1)

    if (travelingDirection=='F'):
        travelingDirection = facingDirection

    if (travelingDirection=='N'):
        coord[0] += distance
    if (travelingDirection=='E'):
        coord[1] += distance
    if (travelingDirection=='S'):
        coord[0] -= instruction[1]
    if (travelingDirection=='W'):
        coord[1] -= instruction[1]

print(coord)