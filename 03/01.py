import string

def get_file_content(file_path):
    try:
        with open (file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))


tree_count = 0
fileData = get_file_content('input.txt')
rawlines = fileData.splitlines()
right_offset =0
for tree_line in rawlines:
    working_line = tree_line
    while (right_offset>=len(working_line)):
        working_line = working_line + tree_line
    #print(f'working_line: {working_line}')
    item_at_pos = working_line[right_offset:right_offset+1]
    print(f'item_at_pos: {item_at_pos}')
    print(f'{right_offset} - {len(working_line)}')
    if (item_at_pos=='#'):
        tree_count +=1

    right_offset += 3

print(f'tree_count: {str(tree_count)}')
    #0 min
    #1 max
    #2 letter
    #3 password
#13-17 s: ssssssssssssgsssj
#7-9 p: pnlzhcppvl
