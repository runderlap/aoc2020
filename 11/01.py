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

def numberArray(line):
    array = []
    for character in line:
        if character=='L':
            array.append(1)
        else:
            array.append(0)
    return array

def valueIfExists(floorPlan, rowNum, colNum):
    if (
        rowNum >= 0 and
        colNum >= 0 and
        len(floorPlan)>rowNum and 
        len(floorPlan[rowNum])>colNum
    ):
        return 1 if floorPlan[rowNum][colNum]>5 else 0
    else: 
        return 0

def getAdjectent(floorPlan, rowNum, colNum):
    adjectent = 0
    adjectent += valueIfExists(floorPlan, rowNum-1, colNum-1)
    adjectent += valueIfExists(floorPlan, rowNum-1, colNum)
    adjectent += valueIfExists(floorPlan, rowNum-1, colNum+1)
    adjectent += valueIfExists(floorPlan, rowNum, colNum-1)
    adjectent += valueIfExists(floorPlan, rowNum, colNum+1)
    adjectent += valueIfExists(floorPlan, rowNum+1, colNum-1)
    adjectent += valueIfExists(floorPlan, rowNum+1, colNum)
    adjectent += valueIfExists(floorPlan, rowNum+1, colNum+1)
    return adjectent



fileData = get_file_content('input.txt')
floorPlan = list(map(numberArray,fileData.splitlines()))

changing = True
rounds = 0
while changing:
    rounds+=1
    changing = False
    newFloorplan = []
    for rowNum in range(len(floorPlan)):
        newRow = []
        for colNum in range(len(floorPlan[rowNum])):
            currentState = floorPlan[rowNum][colNum]
            adjectent = getAdjectent(floorPlan, rowNum, colNum)
            newState = currentState
            if currentState==1 and adjectent==0: #empty seat with no adjectents becomes taken
                newState = 10
                changing = True
            if currentState==10 and adjectent>3: #taken seat with >3 adjectents becomes empty
                newState = 1
                changing = True
            newRow.append(newState)
        newFloorplan.append(newRow)
    floorPlan = newFloorplan

totalTakenSeats = 0
for row in floorPlan:
    print(row)
    for col in row:
        if col==10:
            totalTakenSeats+=1


print(str(rounds))
print(str(totalTakenSeats))