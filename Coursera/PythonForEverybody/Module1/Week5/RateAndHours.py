hrs = input("Enter Hours:")
r = input("Enter Rate:")

try:
    h = float(hrs)
    rate = float(r)
except:
    print("Error, please enter numeric input for hours and rate")
    quit() # do not continue on
    
regularHours = 0.0
overTimeHours = 0.0

total_regular = 0.0
total_overTime = 0.0

if h > 40:
    overTimeHours = h - 40
    regularHours = 40
else:
    regularHours = h 
    overTimeHours = 0 

total_regular = regularHours * rate
total_overTime = overTimeHours * (rate * 1.5)

print(total_regular + total_overTime)
