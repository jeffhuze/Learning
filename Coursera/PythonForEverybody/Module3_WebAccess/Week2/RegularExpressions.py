# must import 
import re 

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('From: ', line):
        print(line)

print('next older version......./n')

hand = open('mbox-short.txt') # to get this below to run like the one above, need to use the open() function again
for line in hand:
    line = line.rstrip()
    # print(line)
    if line.find('From: ') >= 0:
        print(line)
        continue

hand = open('mbox-short.txt') # to get this below to run like the one above, need to use the open() function again
for line in hand:
    line = line.rstrip()
    if re.search('^From: ', line):  # adding the carrot ^ is like the line.startswith('From:') function 
        print(line)

# To get all of these
# X-Sieve: CMU Sieve 2.3
# X-DSPAM-Result: Innnocent
# X-DSPAM-Confidence: 0.8475
# X-Content-Type-Message-Body: text/plain
# Use this regex:  ^X.*:    # starts with X, any number of characters, ending with a :
# Use this regex:  ^X-\S+:  # starts with X-, any number of NON-WHITESPACE characters, ending with a :

###########################################
# [0-9]+ find any digit with 1 or more characters (digits); a + means >= 1

x = 'My 2 favorite numbers are 19 and 42.'
y = re.findall('[0-9]+',x) 
print(y)

# ^F.+:  # says First character is an F, . says any character, + says 1 or more, and : ends with :  , this is GREEDY without the ?
# ^F.+?:  #here the ? says one or more characters but NOT greedy

# to find or extract an email address
# \S is nonblank characters
# + is one or more
# y = re.findall('\S+@\S+, x)
# print(y)

# paratheses are not part of the match but they tell where to start and stop what string to extract
# y = re.findall('^From (\S+@\S+), x)

# get the part after the @ symbol
# y = re.findall( '@([^ ]*)', lin )
# the [^ ] says match non-blank character
# the * says match many of them
# y = re.findall( 'From .*@([^ ]*)', lin )

import re
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall( '^X-SPAM-Confidence: ([0-9]+)', line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))


# escape
x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+', x)
print(y)
