name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fhand = open(name)

myCounter = 0
counts = dict()
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        times = words[5]
        # print(times)
        hoursMinutesSeconds = times.split(':')
        hours = hoursMinutesSeconds[0]
        # print(hours)
        counts[hours] = counts.get(hours,0) + 1  # myCounter
        # myCounter = myCounter + 1
        # for hour in hours:
        #     counts[hour] = counts.get(hour,0) + 1
            # print(hour)

# print('keys..')
# print( counts.keys() )
# print('values..')
# print( counts.values() )
# print('items..')
# print( counts.items() )

lst = list()
for key, val in counts.items():
    newtup = (key, val)
    lst.append(newtup)

# print(lst)

lst = sorted(lst, reverse=False)
# print(lst)

for a,b in lst:
    print(a,b)

# for key, val in lst[:10]:
#     # print(key, val)
#     continue
       