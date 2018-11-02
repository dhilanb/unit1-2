day= int(input("Pick a number between 1 and 365. "))
total= day-5
if total%7+1==7:
    print(0)
else:
    print(total%7+1)