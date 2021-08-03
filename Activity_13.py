from math import sqrt
def main():
    print("Enter any number: ", end = "")
    a = input_number()
    p = isprime(a)
    display(a, p)
def input_number():
    return int(input())

def isprime(a):
    if a == 1:
        return False
    for i in range(2, round(sqrt(a)) + 1,1):
        if a%i == 0:
            return False
    return True

def display(a, p):
    if p:
        print(f"{a} is a prime number")
    else:
        print(f"{a} is not a prime number")

main()
    
