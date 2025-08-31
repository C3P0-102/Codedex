#AREA CALCULATOR
from math import pi 
print("==================")
print("Area Calculator 📐")
print("==================")
print("\n")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
print("\n")
a=int(input("Which shape: "))

if a==1:
    Base=int(input("Base: "))
    Height=int(input("Height: "))
    area=(Height*Base)/2
    print("The area is",area)
elif a==2:
    Length=int(input("Length: "))
    Width=int(input("Width: "))
    area=(Length*Width)
    print("The area is",area)
elif a==3:
    Side=int(input("Side: "))
    area=Side**2
    print("The area is",area)
elif a==4:
    Radius=int(input("Radius: "))
    area=pi*(Radius**2)
    print("The area is",area)
if a==5:
    print("Thank you!!")