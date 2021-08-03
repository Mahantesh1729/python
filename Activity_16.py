
def main():
    print("Enter some strings")
    lis1 = input_list()
    lis2 = convert(lis1)
    display(lis2)
def input_list():
    return input().split(";")

def convert(lis1):
    lis2 = [tuple(x.split("=")) for x in lis1]
    return lis2

def display(lis2):
    print(lis2)

main()
