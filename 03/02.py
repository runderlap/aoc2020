import string

def get_file_content(file_path):
    try:
        with open (file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))


fileData = get_file_content('input.txt')
rawlines = fileData.splitlines()
def gettreesWithOffset(rawlines, offset, downset):
    tree_count = 0
    right_offset = 0
    down_offset = 0
    while len(rawlines)>down_offset:
    #for tree_line in rawlines:
        tree_line = rawlines[down_offset]
        working_line = tree_line
        while (right_offset>=len(working_line)):
            working_line = working_line + tree_line
        #print(f'working_line: {working_line}')
        item_at_pos = working_line[right_offset:right_offset+1]
        if (item_at_pos=='#'):
            tree_count +=1

        right_offset += offset
        down_offset += downset

    print(f'offset {offset} gives: {tree_count}')
    return tree_count

product = (
    gettreesWithOffset(rawlines, 1,1) *
    gettreesWithOffset(rawlines, 3,1) *
    gettreesWithOffset(rawlines, 5,1) *
    gettreesWithOffset(rawlines, 7,1) *
    gettreesWithOffset(rawlines, 1,2)
)

print(f'product: {str(product)}')
