# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
fLineCombo = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    replaceLine = line.replace('X-DSPAM-Confidence:','')
    stripLine = replaceLine.strip()
    fLine = float(stripLine)
    fLineCombo = fLineCombo + fLine 
    # print(line)
    # print(stripLine)
print("Average spam confidence:", fLineCombo/count)



# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be open:', fname)
    quit()

for line in fh:
    lineStripped = line.rstrip()
    lineStripped = lineStripped.upper()
    # if line.startswith('From'):
    #     print(lineStripped)
    # if not '@uct.ac.az' in lineStripped:
    #     continue
    # print(lineStripped)
    print(lineStripped)    

# count = 0
# for line in fh:
#     if line.startswith('Subject:'):
#         count = count + 1
# print('There were', count, 'subject line in',fname)


