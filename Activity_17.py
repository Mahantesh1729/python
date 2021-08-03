
def main():
    print("Enter some strings")
    lis1 = input_list()
    lis2 = convert(lis1)
    print("List of tuples")
    display(lis2)
    string = convertback(lis2)
    print("Back to string")
    display(string)
    
def input_list():
    return input().split(";")

def convert(lis1):
    lis2 = []
    for i in range(len(lis1)):
        lis2.append(tuple(lis1[i].split("=")))
    return lis2

def display(lis2):
    print(lis2)

def convertback(lis):
    s = ""
    for i in range(len(lis) - 1):
        s += lis[i][0] + "=" + lis[i][1]
        s += ';'
    i += 1
    s += lis[i][0] + "=" + lis[i][1]
    return s;

main()
