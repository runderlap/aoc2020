import string
import os
import time

startTime = time.time()

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

def checkNextmatch(timestamp, busnumber, remaining):
    matchOnCorrectPosition = False
    

fileData = get_file_content('input.txt')
data = fileData.splitlines()
starttime = int(data[0])
busses = list(map(nonX,data[1].split(',')))

bss=[]
highestBus = 0
highestBusOffset = 0
for i in range(len(busses)):
    if busses[i]>0:
        if busses[i]>highestBus:
            highestBus = busses[i]
            highestBusOffset = i
        bss.append((busses[i],i))

print(highestBus)
#bss.sort(reverse = True)
print(bss)

k = 0
t=0
match = False
while not match:
    match = True
    j =0
    for b in bss:
        j+=1
        busNumber = b[0]
        timeOffset = b[1]
        if ((t-highestBusOffset+timeOffset)) % busNumber != 0:
            if j>k:
                k=j
                print(k)
            match = False
            break
    t+= highestBus

print(str(t-highestBus-highestBusOffset))

print("--- %s seconds ---" % (time.time() - startTime))