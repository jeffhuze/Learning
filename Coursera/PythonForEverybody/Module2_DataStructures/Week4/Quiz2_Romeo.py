fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    # print(line.rstrip())
    line = line.rstrip()
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
    # if words not in lst:
    #     lst.append(words)
lst.sort()    
print( lst )

