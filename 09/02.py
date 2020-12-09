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
numberToSolve = 373803594
windowsize = 25
i = 0
matchFound = False
currentnumber = lines[i+windowsize:i+windowsize+1]
windowFrom = 0
windowTo = windowFrom+2
while not matchFound:
    numberfound = 0
    while numberfound < numberToSolve:
        numberfound = sum(lines[windowFrom:windowTo])
        if numberfound == numberToSolve:
            matchFound = True
            print(
                str(
                    min(lines[windowFrom:windowTo])+max(lines[windowFrom:windowTo])
                    )
                )
        windowTo +=1
    windowFrom+=1
    windowTo = windowFrom+2
