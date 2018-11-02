year= int(input("Type a random year. "))
tens= year//1000
ones= year//100
century= tens+ones
if year%1000==0:
    print(str(century-2)+"th century.")
elif year%100==0:
    print(str(century-1)+"th century")
else:
    print(str(century)+"th century.")
