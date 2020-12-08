import string
import os
import re

def cleanBagName(bagName):
    return bagName.replace('.','').replace('1 ','').replace('2 ','').replace('3 ','').replace('4 ','').replace('5 ','').replace('6 ','').replace('7 ','').replace('bags','bag').replace('bag ','bag')

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

mybag = 'shiny gold bag'
correctContainers = [mybag]
def findCorrectContainers(current_containers):
    for line in lines:
        split = line.split('contain ')
        container = split[0].replace('bags','bag').replace('bag ','bag')
        allowed_contents = list(map(cleanBagName, split[1].split(', ')))

        for allowed in allowed_contents:
            print(allowed)
            if allowed in current_containers and container not in current_containers:
                current_containers.append(container)
    return current_containers


new_containers = 1
current_containers = 0
while current_containers < new_containers:
    print(correctContainers)
    current_containers = new_containers
    correctContainers = findCorrectContainers(correctContainers)
    new_containers = len(correctContainers)
print(len(correctContainers))