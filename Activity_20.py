def main():
    print("How many key value pairs do you want to enter: ")
    n = number_input()
    dis = create_dictionary(n)
    print("Dictionary created: ")
    display(dis)
    dis1 = sort_by_value(dis)
    print("Dictionary sorted by value: ")
    display(dis1)
def number_input():
    return int(input())

def create_dictionary(n):
    dis = {}
    for i in range(n):
        lis = input().split(" ")
        dis[lis[0]] = lis[1]
    return dis

def sort_by_value(dis):
    lis = list(dis.items())
    n = len(dis)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lis[i][1] > lis[j][1]:
                k = lis[i]
                lis[i] = lis[j]
                lis[j] = k
    return dict(lis)

def display(s):
    print(s)
main()
