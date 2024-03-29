# t = [9, 41, 12, 3, 74, 15]
# print( t[2:4] )

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        words = line.split()
        email = words[1]
        print(email)
        count = count + 1
print("There were", count, "lines in the file with From as the first word")


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From'):
#         continue
#     words = line.split()
#     print(words[2])
