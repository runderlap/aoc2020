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

def nonX(bus):
    if bus =='x':
        return 0
    else:
        return int(bus)

fileData = get_file_content('input.txt')
data = fileData.splitlines()
starttime = int(data[0])
busses = list(map(nonX,data[1].split(',')))

print(busses)
lowestWait = 9999999
bestBus = 0
for bus in busses:
    if bus >0:
        wait = bus -(starttime % bus)
        if wait < lowestWait:
            lowestWait = wait
            bestBus = bus

print(str(bestBus*lowestWait))


