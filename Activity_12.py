def main():
    print("Enter any three numbers")    
    lis = input_list()
    a, b, c = lis
    largest = largest_number(a, b, c)
    display(largest, a, b, c)

def input_list():
    return list(map(int, input().split(" ")))
    
def largest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c    

def display(largest, a, b, c):
    print(f"{largest} is the greatest number among {a}, {b}, {c}")

main()
