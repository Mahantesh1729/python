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
    lis2 = [tuple(x.split("=")) for x in lis1]
    return lis2

def display(lis):
    print(lis)

def convertback(lis):
    s = ""
    for i in range(3):
        s += lis[i][0] + "=" + lis[i][1]
        s += ';'
    i += 1
    s += lis[i][0] + "=" + lis[i][1]
    return s;

main()
