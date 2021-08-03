print("Enter any three numbers")
lis = list(map(int, input().split(" ")))
a, b, c = lis

if a > b and a > c:
    print(f"{a} is the greatest number among {a}, {b}, {c}")
elif b > c:
    print(f"{b} is the greatest number among {a}, {b}, {c}")
else:
    print(f"{c} is the greatest number among {a}, {b}, {c}")    

    
