import re
def main():
    print("Enter some strings: ")
    s = string_input()
    s = re.split(';|=', s)
    dis = make_dict(s)
    print("Dictionary created")
    display(dis)
    print("Converted back to string")
    s = revert(dis)
    display(s)
    
def string_input():
    return input()

def make_dict(s):
    keys = []
    values = []
    for i in range(len(s)):
        if(i % 2 == 0):
            keys.append(s[i])
        else:
            values.append(s[i])

    dis = { k:v for (k, v) in zip(keys, values)}
    return dis

def revert(dis):
    s = ""
    for i in dis:
        s += i + "="+dis[i]+ ";"
    s = s[:-1]
    return s

def display(dis):
    print(dis)
        

main()
