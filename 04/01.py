import string
import os
import re


def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path, filename = os.path.split(full_path)
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
passports = fileData.split('\n\n')

def isValidHeight(heightstring):
    if (heightstring.replace('cm','')).isnumeric() and int(heightstring.replace('cm',''))>149 and int(heightstring.replace('cm',''))<194:
        return True
    if (heightstring.replace('in','')).isnumeric() and int(heightstring.replace('in',''))>58 and int(heightstring.replace('in',''))<77:
        return True
    return False

def validateFieldAndValue(fieldAndValue):
    field = fieldAndValue[0]
    value = fieldAndValue[1]
    '''
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    '''
    validEcl = [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
        ]

    if field=='byr' and value.isnumeric() and int(value)>1919 and int(value)<2003 :
        return True
    if field=='iyr' and value.isnumeric() and int(value)>2009 and int(value)<2021 :
        return True
    if field=='eyr' and value.isnumeric() and int(value)>2019 and int(value)<2031 :
        return True
    if field=='hgt' and value.replace('cm','').replace('in','').isnumeric() and isValidHeight(value) :
        return True
    if field=='hcl' and re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value):#and len(value)==7 and value[0:1]=='#' and re.match('^[a-f0-9]+$',value[1:6]):
        return True
    if field=='ecl' and value in validEcl:
        return True
    if field=='pid' and value.isnumeric() and len(value)==9:
        return True
    if field=='cid':
        return True
    print(f'{field} {value}')
    return False
essentialFields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
    ]
#cid
valid_pp_count = 0
total_count = 0

for rawpp in passports:
    total_count +=1
    pplines = []
    pplinesbynewline = rawpp.split('\n')
    for rawline in pplinesbynewline:
        pplines.extend(rawline.split(' '))

    ppfields = list(map(lambda x: x[0:3], pplines))
    ppfieldsAndValues = list(map(lambda x: x.split(':'), pplines))
    if (pplines[0]!=f'{ppfieldsAndValues[0][0]}:{ppfieldsAndValues[0][1]}'):
            print('wah')
    valid = True
    essentials = True
    for fieldsAndValue in ppfieldsAndValues:
        if valid:
            valid = validateFieldAndValue(fieldsAndValue)
    for check in essentialFields:
        if check not in ppfields:
            essentials = False
    if (valid and essentials):
        valid_pp_count +=1
print(f'{valid_pp_count}/{total_count} valid')
    