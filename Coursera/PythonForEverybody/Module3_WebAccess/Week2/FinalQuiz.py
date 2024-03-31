import re 

fileNameTest = 'regex_sum_42.txt'
fileNameProd = 'regex_sum_2002958.txt'

hand = open(fileNameProd)
numlist = list()

for line in hand:
    line = line.strip()
    stuff = re.findall( '[0-9]+', line)
    for thing in stuff:
        try:
            num = int(thing)
            numlist.append(num)
        except:
            continue

# print('Maximum:', max(numlist))
# print('Count:', len(numlist))
print('Sum:', sum(numlist))
# print(numlist[0:20])
