def main():
    print("Enter the first number")
    a = input_number()
    print("Enter the second number")
    b = input_number()
    summation = add(a, b)
    display(a, b, summation)

def input_number():
    return int(input())

def add(a, b):
    return a + b

def display(a, b, summation):
    print(f"{a} + {b} = {summation}")

main()
