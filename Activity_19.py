def main():
    print("How many key value pairs do you want to enter: ", end = "")
    n = number_input()
    dis = create_dict(n)
    print("Original dictionary")
    display(dis)
    print("Sorted dictionary based on key")
    dis1 = sort_dictionary(dis)
    display(dis1)
    
def number_input():
    return int(input())

def create_dict(n):
    dis = {}
    for i in range(n):
        lis = input().split(" ")
        dis[lis[0]] = lis[1]   
    return dis

def sort_dictionary(dis):
    return {i: dis[i] for i in sorted(dis)}
    
def display(s):
    print(s)
main()
