import string
import os
import re

def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path, f = os.path.split(full_path)
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
lines = fileData.splitlines()
instructions = []
for line in lines:
    split = line.split(' ')
    instructions.append((split[0], int(split[1])))

usedInstructions = []
currentInstruction = 0
acc = 0

while currentInstruction not in usedInstructions:
    usedInstructions.append(currentInstruction)
    print(str(currentInstruction))
    instruction = instructions[currentInstruction]
    move = instruction[0]
    amount = instruction[1]

    if (move=='nop'):
        currentInstruction += 1
    if (move=='acc'):
        acc += amount
        currentInstruction += 1
    if (move=='jmp'):
        currentInstruction += amount



print(str(acc))