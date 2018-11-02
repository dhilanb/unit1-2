name= input("What's your name? ")
shape= input("Would you like a rectangle, square, or cylindrical swimming pool? ")
if shape == "rectangle":
    length= int(input("What's the length of the rectangular pool in feet? "))
    height= int(input("What's the height of the rectangular pool in feet? "))
    width= int(input("What's the width of the rectangular pool in feet? "))
    volume= length*width*height*7.5
    print(name+" the volume of the  rectangular pool is "+str(volume)+" gallons.")
if shape == "square":
    sides= int(input("What's the length of one of the sides of the square pool "+name+" ?"))
    volume= sides**3*7.5
    print(name+" the volume of the square pool is "+str(volume)+" gallons.")
if shape == "cylindrical":
    radius= int(input("What's the radius of the cylindrical pool? "))
    volume= (radius**2)*3.14*5.875
    print(name+" the volume of the cylindrical pool is "+ str(volume)+" gallons.")
