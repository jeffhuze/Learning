#lists review
cards = list()
cards.append(12)
cards.append(3)
cards.append(75)
print(cards)

#dictionary
cabinet = dict()
cabinet['summer'] = 12
cabinet['fall'] = 3
cabinet['spring'] = 75
print(cabinet)

jjj = { 'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj)
ooo = { }
print(ooo)

#check to see if a key is in the dictionary
ccc = dict()
# print(ccc['csev']) # error b/c not in dict
'csev' in ccc # boolean, returns False

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name,0) + 1
    # if name in names:
    #     counts[name] = 1
    # else:
    #     counts[name] = counts[name] + 1

    # if name in counts:
    #     x = counts[name]
    # else:
    #     x = 0
print(counts)
x = counts.get(name,0)
print(x)


counts = dict()
print('ENter a line of text')
line = input('')

words = line.split()
print('WOrds', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)

countsNames = {'chuck':1, 'fred':42, 'jan':100}
for key in countsNames:
    print(key, countsNames[key])

jjj = {'chuck':1, 'fred':42, 'jan':100}    
print(list(jjj)) # list of the keys
print(list(jjj.keys()))
print(list(jjj.values()))
#returns tuples, or like lists that are readable only
print(list(jjj.items()))


jjj = {'chuck':1, 'fred':42, 'jan':100} 
for aaa, bbb in jjj.items():
    print(aaa,bbb)

stuff = dict()
print(stuff.get('candy',-1))    

stuff = dict()
print(stuff['candy'])    

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

bigcount = None 
bigword = None 
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word 
        bigcount = count  
print(bigword, bigcount)


