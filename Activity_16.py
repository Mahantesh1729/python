
def main():
    print("Enter some strings")
    lis1 = input_list()
    lis2 = convert(lis1)
    display(lis2)
def input_list():
    return input().split(";")

def convert(lis1):
    lis2 = []
    for i in range(len(lis1)):
        lis2.append(tuple(lis1[i].split("=")))
    return lis2

def display(lis2):
    print(lis2)

main()
