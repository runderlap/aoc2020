import string

def get_file_content(file_path):
    try:
        with open (file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

def getCrashes(robots, indexToCheck):
    colissions = 0
    for r in range(len(robots)):
        if (r!=indexToCheck
        and robots[r]== robots[indexToCheck]
        ):
            colissions +=1
    return colissions

valid_count = 0
fileData = get_file_content('input.txt')
rawData = fileData.splitlines()
rawRobots = fileData.split(']')[0:-1]
rawMovements = fileData.split(']')[-1].split(')')

robots = []
for robot in rawRobots:
    items = robot.replace('[','').split(',')
    x = int(items[0])
    y = int(items[1])
    robots.append((x,y))

crashes = 0
movepos = 0
while movepos < len(rawMovements)-1:
    for r in range(len(robots)):
        movement = rawMovements[movepos].replace('(','').split(',')
        if movement[0] !='':
            robot= (
                robots[r][0] + int(movement[0]),
                robots[r][1] + int(movement[1])
            )
            robots[r] = robot
            crashes += getCrashes(robots,r)
        movepos +=1

for item in []:
    splits = item.split(' ')
    minmax = splits[0].split('-')
    min = int(minmax[0])
    max = int(minmax[1])
    letter = splits[1].split(':')[0]
    password = splits[2]
    occurrences = password.count(letter)
    is_valid = occurrences >= min and occurrences <= max
    if (is_valid):
        print(f'{item} is valid')
        valid_count +=1
    else:
        print(f'=={item} is invalid')

print(f'valid: {str(valid_count)}')