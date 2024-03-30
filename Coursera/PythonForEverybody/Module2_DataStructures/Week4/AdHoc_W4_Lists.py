# lists are surrounded by square brackets []
# a list can be any python object, even another list
# a list can be empty
# lists are mutable, we can change an element of a list using the index operator

# to produce the list [12,3] .... i..e. from position 2, the 12, to position 74 which is excluded
t = [9, 41, 12, 3, 74, 15]
print( t[2:4] )


friends = ['Joseph', 'Glenn','Sally']
for friend in friends:
    print('Happy New Year:', friend)

for i in range( len(friends) ):
    friend = friends[i]
    print('Happy New Year:', friend)

a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

# we can creaet an empty list and then add elements using the append method
# the list stays in order and new elements are added at the end of the list
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

#True
print(99 in stuff) 

nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print( sum(nums) / len(nums) )

total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value 
    count = count + 1

average = total / count
print('Average: ', average)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)

average2 = sum(numlist) / len(numlist)
print('Average: ', average2)

abc = 'With three words'
stuffing = abc.split()
print(stuffing)
print(len(stuffing))

for w in stuffing:
    print(w)

line = 'A lot           of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split(';')
print(thing)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[2])


# words = line.split()
# email = words[1]
# pieces = email.split('@')
# print(pieces[1])
