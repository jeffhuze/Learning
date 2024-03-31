import re
myString = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
stuff = re.findall( '@(\S+)', myString)
print(stuff)

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)

test = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
testSearch = re.findall('\S+?@\S+',test)
print(testSearch)
