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
nums = list(map(lambda x: int(x),fileData.splitlines()))
nums.sort()
dif1 = 1 #outlet to first adapter
dif3 = 1 #last adapter to device

for i in range(len(nums)):
    if (i!=0):
        dif = nums[i] - nums[i-1]
        print(f'{i}: {dif}')
        if dif==3:
            dif3 +=1
        if dif==1:
            dif1 +=1
        





print(str(dif3*dif1))