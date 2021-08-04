
def main():
    print("Enter some strings")
    lis1 = input_list()
    lis2 = convert(lis1)
    Dict = dict(lis2)
    print("Displaying dictionary")
    display(Dict)
    print("Displaying original string after conversion from dict")
    string = convert_to_string(Dict)
    display(string)
def input_list():
    return input().split(";")

def convert(lis1):
    lis2 = [tuple(x.split("=")) for x in lis1]
    return lis2

def convert_to_string(Dict):
    s = ""
    for i in Dict:
        s += i + "=" + Dict[i] + ";"
    s = s[:-1]
    return s

def display(s):
    print(s)

main()
