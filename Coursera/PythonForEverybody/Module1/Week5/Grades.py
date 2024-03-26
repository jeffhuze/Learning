score = input("Enter Score: ")

try:
    s = float(score)
except:
    print('Error, pls enter a number')

if s < 0.0 or s > 1:
    print('Error, needs to be between 0.0 and 1.0')

grade = ''

if s >= .9:
    grade = 'A'
elif s >= .8:
    grade = 'B'
elif s >= .7:
    grade = 'C'
elif s >= .6:
    grade = 'D'
elif s < .6:
    grade = 'F'
else:
    grade = 'Error, invalid'

print(grade)
