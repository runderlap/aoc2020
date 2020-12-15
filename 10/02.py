import string
import os
import tst

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
nums.append(0) # outlet skipped because we will alway have that one
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

if skippableStreak>0:
    print(nums[i-skippableStreak:i])
    totalPossibilities *= tst.numberOfPossibilities(skippableStreak)
print(str(totalPossibilities))

        # #i+2 is a >+3 jump, so the only possibility is i+1 thus creating a choking point
        # #from OR to this step is a 3-jump, so it can't be skipped
        # ##### if the diff to currentnum or 
        # if (nums[i+2]-nums[i]>3):
        #     chockingPoints.append((i,0))
        # dif = nums[i+1] - nums[i]
        # print(f'{i}: {dif}')



# #make unique combinations of 1,2,3 steps where the total adds up to exact the dif between the min and max of the array

# total steps between floor and ceiling (array.length) determines the amount of digits.
# So like the betow example: 0-3 = 3 steps = 000

# Possibilities (number = steps, position)
# X X X
# 0 0 0


# from 0 to 2
# 11
# 2
# 0

# from 0 to 3: #4 possibilities. diff of 3(2 skippables)
# -111
# 1,2
# -12
# 1
# -21
# 2
# -3
# x
# #with digit counters (base3?) here:





# from 26 to 30: #7 possibilities.  diff of 4(3 skippables)
# -1111
# 27,28,29
# -112
# 27,28
# -121
# 27,29
# -13
# 27
# -211
# 28,29
# -22
# 28
# -31
# 29

# hypothetically, from 40 to 45: #13 possibilities diff of 5(4 skippables)
# 41,42,43,44
# 41,42,43
# 41,42,44
# 41,42
# 41,43,44
# 41,43
# 41,44
# 42,43,44
# 42,43
# 42,44
# 42
# 43,44
# 43



# hypothetically, from 50 to 60
# 111111111
# 51,52,53,54,55,56,57,58,59
# 2222
# 52,54,56,58
# 333
# 53,56,59

# # 00:0 +1 --start, so we must get here
# # 01:1 +1 --skip?
# # 02:2 +1 --skip?
# # 03:3 +3 --we must get here
# # 04:6 +3 --we must get here
# # 05:9 +1 --we must get here
# # 06:10 +1 --skip?
# # 07:11 +1 --skip?
# # 08:12 +3 --we must get here
# # 09:15 +1 --we must get here
# # 10:16 +1 --skip?
# # 11:17 +3 --we must get here
# # 12:20 +3 --we must get here
# # 13:23 +3 --we must get here
# # 14:26 +1 --we must get here
# # 15:27 +1 --skip?
# # 16:28 +1 --skip?
# # 17:29 +1 --skip?
# # 18:30 +3 --we must get here
# # 19:33 +1 --we must get here
# # 20:34 +1 --skip?
# # 21:35 +1 --skip?
# # 22:36 +3 --we must get here
# # 23:39 +1 --we must get here
# # 24:40 
