print("Enter any five numbers: ", end="")
lis = input()
lis = lis.split(" ")
lis = list(map(int, lis))
sli = lis[0: 3]

print("sliced list = ", sli)
lis[0] = 0
lis[-1] = 0
sli[0] = 0
sli[-1] = 0

print("replaced list-1 = ", lis)
print("replaced lsit-2 = ", sli)

