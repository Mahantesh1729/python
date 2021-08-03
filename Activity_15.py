def main():
    print("Enter something")
    lis = input_list_strings()
    display(lis)
def input_list_strings():
    return input().split(" ")

def display(lis):
    print("sorted() function doesnt affect the original list\n")
    print("sorted(): ",sorted(lis),"\n")
    print("Original list: ", lis, "\n")
    print("sort() method affects the original list\n")
    lis.sort()
    print("sort(): ", lis, "\n")



main()
