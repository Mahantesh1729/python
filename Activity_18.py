import re
def main():
    print("Enter some strings: ")
    s = string_input()
    dis = make_dict(s)
    print("Dictionary created")
    display(dis)
    print("Converted back to string")
    s = revert(dis)
    display(s)
def string_input():
    return input()
def make_dict(lis):
    dis = {k:v for k, v in (a.split('=')for a in lis.split(';'))}
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
