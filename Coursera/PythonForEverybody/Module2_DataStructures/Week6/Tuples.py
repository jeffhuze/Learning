# tuples function like a list except use ()
# tuples cannot be changed, they are immutable; same with strings, they are immutable too
# however, lists are mutable

a,b = 3,4
print(b)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()
print(y)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print( days[2] )


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = (1, 9, 2)
print(y)
print(max(y))

# lists are mutable; works, no error
x = [9,8,7]
x[2] = 6
print(x)

# this would error, strings are immutable
y = 'ABC'
# y[2] = 'D' # would throw an error, can't change string

# this would error, tuples are immutable
z = (5, 4, 3)
#z[2] = 0 # would error, can't change tuple

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k,v)

tups = d.items()
print(tups)   

d = { 'a':10, 'c':22, 'b':1 }
print( d.items() )
print( sorted(d.items()) )

for k,v in sorted( d.items() ):
    print(k,v)

c = { 'a':10, 'b':1, 'c':22 }
tmp = list()
for k,v in c.items():
    tmp.append( (v,k) )

print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, ke in lst[:10]:
    print(key, val)

 # shorter version
 # read up on 'list comprehension', which creates dynamic lists
c = { 'a':10, 'b':1, 'c':22 }
print( sorted( [ (v,k) for k,v in c.items() ] ) )
