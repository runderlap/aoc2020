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
    #0 min
    #1 max
    #2 letter
    #3 password
#13-17 s: ssssssssssssgsssj
#7-9 p: pnlzhcppvl
