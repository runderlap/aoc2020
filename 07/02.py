import string
import os
import re

def cleanBagName(bagName):
    amount = bagName[0:1]
    name = bagName.replace('.','').replace('1 ','').replace('2 ','').replace('3 ','').replace('4 ','').replace('5 ','').replace('6 ','').replace('7 ','').replace('bags','bag').replace('bag ','bag')
    if amount=='n':
        amount = '1'
    return (int(amount), name)

def get_file_content(file_path):
    try:
        full_path = os.path.realpath(__file__)
        path = os.path.split(full_path)[0]
        with open (path + '/' + file_path, "r") as file_stream:
            return file_stream.read()
    except Exception as e:
        raise FileNotFoundError(file_path + " cannot be parsed: " + str(e))

fileData = get_file_content('input.txt')
lines = fileData.splitlines()
rules = {}
for line in lines:
    split = line.split('contain ')
    container = split[0].replace('bags','bag').replace('bag ','bag')
    allowed_contents = list(map(cleanBagName, split[1].split(', ')))
    rules[container]= allowed_contents

def getBagContent(bagName):
    result = 1
    bagContent = rules[bagName]
    if bagContent[0][1] == 'no other bag':
        return result
    for bag in bagContent:
        result += bag[0] * getBagContent(bag[1])
    return result


# shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags.


# rules = {}
# rules['emmer'] = [(2,'zak'),(1,'krat')]
# rules['zak'] = [(1,'no other bag')]
# rules['krat'] = [(3,'koffer'),(4,'kliko')]
# rules['koffer'] = [(3,'kliko')]
# rules['kliko'] = [(1,'no other bag')]
# baglist = getBagContent('emmer')

# print(baglist)


mybag = 'shiny gold bag'
baglist = getBagContent(mybag)

print(baglist)