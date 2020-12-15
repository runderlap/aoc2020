
def getHighestPath(numberOfNodes):
    if numberOfNodes<4:
        return str(numberOfNodes)
    totalValue=0
    chain = []
    while totalValue<numberOfNodes:
        if numberOfNodes-totalValue<4:
            chain.append(str(numberOfNodes-totalValue))
            totalValue += numberOfNodes-totalValue
        else:
            chain.append(str(3))
            totalValue += 3
    return ''.join(chain)

def decToBase(n, b=3):
    e = n//b
    q = n%b
    if n == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return decToBase(e,b) + str(q)

def sumOfDigitsFits(base3,pathLength):
    total = 0
    for character in str(base3):
        total +=int(character)
    return total==pathLength

def getBase3Number(number):
    maxBase3 = '1' * number
    return int(maxBase3,3)

def highestBase3(number):
    maxBase3 = '1' * number
    return maxBase3

def getAllValidSeries(maxPathAsDecimal, pathLength, base):
    validNumbers = []
    for i in range(maxPathAsDecimal+1):
        base3 = decToBase(i, base).replace('0','')
        if (sumOfDigitsFits(base3,pathLength) and base3 not in validNumbers):
            validNumbers.append(base3)
    return validNumbers


def numberOfPossibilities(distance):
    base = 4
    pathLength = distance+1
    #make a path with all 1's
    longestPath = highestBase3(pathLength)
    #convert this from baseX to decimal
    longestPathDecimal = int(longestPath, base)
    #loop from 0 to this number
    paths = getAllValidSeries(longestPathDecimal, pathLength, base)
    return len(paths)

