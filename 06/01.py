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
groups = fileData.split('\n\n')

totalWorth = 0
for group in groups:
    #groupchars = group.split()
    uniqueAnswers = []
    for char in group:
        if char != '\n' and char not in uniqueAnswers:
            uniqueAnswers.append(char)
    totalWorth += len(uniqueAnswers)
print(totalWorth)