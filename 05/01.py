import string
import os
import re


def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
lines = fileData.splitlines()

highest = 0
for line in lines:
    part1 = int(line[0:7].replace('F','0').replace('B','1'),2)
    part2 = int(line[7:].replace('R','1').replace('L','0'),2)
    current = (part1*8)+part2
    #print(part1)
    if (current>highest):
        highest=current
print(highest)