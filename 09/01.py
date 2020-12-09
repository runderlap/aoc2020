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
lines = list(map(lambda x: int(x),fileData.splitlines()))
windowsize = 25
i = 0
matchFound = True
currentnumber = lines[i+windowsize:i+windowsize+1]
while matchFound:
    matchFound = False
    numbersToUse = lines[i:i+windowsize]
    currentnumber = lines[i+windowsize]
    for j in range(len(numbersToUse)):
        for k in range(len(numbersToUse)):
            if (j!=k and numbersToUse[j]+numbersToUse[k]==currentnumber):
                matchFound = True
    i+=1





print(str(currentnumber))