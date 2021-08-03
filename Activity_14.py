from math import pi
def main():
    print("Enter the dimensions of tromboloid: ")
    l = input_number("length")
    b = input_number("breadth")
    h = input_number("height")
    k = cdimen(l, b, h)
    v = tromvol(b, h, k)
    r = sphrad(v)
    display(v, r)
        
def input_number(dim):
    return int(input(dim + ": "))

def cdimen(l, b, h):
    return l**2 + b**2 + h**2

def tromvol(b, h, k):
    return ((b**2)*(h**2)) /(k**(0.5))

def sphrad(v):
    return ((v * 0.75) / pi )**(1./3.)

def display(v, r):
    print(f"Volume of tromboloid is {v:.3f}")
    print(f"Radius of sphere is {r:.3f}")
    

main()
