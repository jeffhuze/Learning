largest_so_far = None # -1
print('Before', largest_so_far)

for the_num in [9,41,12,3,74,15]:
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)


###

smallest_so_far = None # 10000
print('Before', smallest_so_far)

for the_num in [9,41,12,3,74,15]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print('After', smallest_so_far)

tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
    print(tot)
print(tot)

smallest_so_far = -1
for the_num in [9, 41, 12, 3, 74, 15] :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

###
num = 0
tot = 0.0

while True:
    sval = input('Enter a number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    print(fval)
    num = num + 1
    tot = tot + fval

print('All Done')
print(tot,num,tot/num)

####

largest = None
smallest = None
while True:
    # print('smallest begin block',str(smallest))
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        fval = int(num)
    except:
        print('Invalid input')
        # print('Invalid input with smallest at', str(smallest))
        continue
    if smallest is None:
        smallest = fval
        # print("smallest (none)",str(smallest))
    if fval <= smallest:
        smallest = fval
        # print("smallest (normal)",str(smallest))
    if largest is None:
        largest = fval
    elif fval >= largest:
        largest = fval    
    # print('smallest end block',str(smallest))
    # print(num)

print("Maximum is", largest)
print("Minimum is", smallest)
