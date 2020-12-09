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


flippedInstructions = []
positionFound = False

def tryProgram():
    usedInstructions = []
    currentInstruction = 0
    acc = 0
    flipped = False
    while currentInstruction not in usedInstructions:
        usedInstructions.append(currentInstruction)
        if (currentInstruction >= len(instructions)):
            print('WE DID IT!!!')
            print('acc: '+ str(acc))
            positionFound = True
        instruction = instructions[currentInstruction]
        move = instruction[0]
        amount = instruction[1]

        if not flipped and currentInstruction not in flippedInstructions:
            if move=='jmp':
                flipped = True
                flippedInstructions.append(currentInstruction)
                move = 'nop'
            elif move=='nop': 
                flipped = True
                flippedInstructions.append(currentInstruction)
                move = 'jmp'

        if (move=='nop'):
            currentInstruction += 1
        if (move=='acc'):
            acc += amount
            currentInstruction += 1
        if (move=='jmp'):
            currentInstruction += amount
    #Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp)

while not positionFound:
    tryProgram()


print(str(acc))