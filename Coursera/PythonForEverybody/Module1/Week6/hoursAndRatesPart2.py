hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Error, please enter numeric input for hours and rate")
    quit() # do not continue on

def computepay(h, r):
    if h > 40:
        overTimeHours = h - 40
        regularHours = 40
    else:
        regularHours = h 
        overTimeHours = 0
    total_regular = regularHours * r
    total_overTime = overTimeHours * (r * 1.5) 
    total = total_regular + total_overTime
    return total

p = computepay(h, r)
print("Pay", p)


