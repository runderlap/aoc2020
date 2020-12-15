import string
import os
import pathcounter

def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path = os.path.split(full_path)[0]
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
nums = list(map(lambda x: int(x),fileData.splitlines()))
nums.append(0) # outlet
nums.sort()

skippableStreak = 0
totalPossibilities = 1
for i in range(len(nums)-1):
    skippableFromPrev = nums[i]-nums[i-1]==1
    skippableToNext = nums[i+1]-nums[i]==1
    print(f'{str(nums[i-1])} _ {str(nums[i])} _ {str(nums[i+1])}')
    if (skippableFromPrev and skippableToNext):# or i==0:
        skippableStreak += 1
    elif skippableStreak>0:
        print(nums[i-skippableStreak:i])
        totalPossibilities *= tst.numberOfPossibilities(skippableStreak)
        skippableStreak = 0
#one last time for the 'tail' of the series
if skippableStreak>0:
    print(nums[i-skippableStreak:i])
    totalPossibilities *= tst.numberOfPossibilities(skippableStreak)

print(str(totalPossibilities))
