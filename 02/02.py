import string

def get_file_content(file_path):
    try:
        with open (file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))


valid_count = 0
fileData = get_file_content('input.txt')
rawlines = fileData.splitlines()
objects = []
for item in rawlines:
    splits = item.split(' ')
    minmax = splits[0].split('-')
    pos1 = int(minmax[0])
    pos2 = int(minmax[1])
    letter = splits[1].split(':')[0]
    password = splits[2]
    inPos1 = password.count(letter,pos1-1,pos1) ==1
    inPos2 = password.count(letter,pos2-1,pos2) ==1
    is_valid = inPos1 != inPos2
    if (is_valid):
        print(f'{item} is valid')
        valid_count +=1
    else:
        print(f'=={item} is invalid')

print(f'valid: {str(valid_count)}')
    #0 min
    #1 max
    #2 letter
    #3 password
#13-17 s: ssssssssssssgsssj
#7-9 p: pnlzhcppvl
