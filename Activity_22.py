from math import pi
def main():
    print("Enter the angle in degrees: ", end = "")
    n = input_angle()
    n = convert_to_radians(n)
    ans = sine(n)
    print("The sine of the given angle is: ", end = "")
    display(ans)

def input_angle():
    return int(input())

def convert_to_radians(n):
    n %= 360
    return (n * (pi / 180))

def sine(n):
    ans = 0
    k = 0
    for i in range(1, 12, 2):
        ans += (((-1)**(k%2))*(n**i)) / fact(i)
        k += 1
    return ans

def fact(i):
    if i == 1:
        return 1
    else:
        return i * fact(i - 1)

def display(ans):
    print(ans)
main()
