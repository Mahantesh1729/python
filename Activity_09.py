from math import pi
print("Enter the dimensions of tromboloid: ")
l = int(input("Length: "))
b = int(input("Breadth: "))
h = int(input("Height: "))
k = l**2 + b**2 + h**2
tromvol = ((b**2)*(h**2)) /(k**(0.5))
print(f"Volume of tromboloid is {tromvol:.3f}")
sphrad = ((tromvol * 0.75) / pi )**(1./3.)
print(f"Radius of sphere is {sphrad:.3f}")
