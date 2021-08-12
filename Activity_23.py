def main():
    print("Enter some number")
    dis = {1:'', 2:'ABC', 3:'DEF', 4:'GHI', 5:'JKL', 6: 'MNO', 7: 'PQRS',
           8: 'TUV', 9: 'WXYZ', 0:''}
    nums = input_number()
    ans = possible_strings(dis, nums, len(nums))
    print("The possible strings are: ")
    display(ans)
def input_number():
    return input()

def possible_strings(dis, nums, n):
    s = ''
    i = 0
    k = [""]
    while i < len(nums):
        count = 1
        if i+1 != len(nums):
            while nums[i] == nums[i + 1]:
                count += 1
                i += 1
                if i+1 == len(nums):
                    break
        q = []
        s = poss_list(dis[int(nums[i])], count)
        for i1 in k:
            for j in s:
                q.append(i1 + j)
        q = list(set(q))
        k = q
        i += 1
    return k

def poss_list(chars, count):
    lis = combination_list(chars, count)
    if count < 3:
        return [lis[i] for i in range(count)]
    elif count == 3 or (len(chars) == 4 and count == 4):
        return lis
    else:
        lis1 = []
        if(len(chars) == 3):
            lis2 = poss_list(chars, count - 3)
        else:
            lis2 = poss_list(chars, count - 4)
        for i in lis:
            for j in lis2:
                lis1.append(i+j)
                lis1.append(j+i)
        return list(set(lis1))

def combination_list(chars, count):
    lis = []
    if count == 1:
        return chars[0]
    elif count == 2:
        lis = chars[0] * 2, chars[1] 
        return lis
    elif((len(chars) == 3 and count >= 3) or (len(chars) == 4 and count == 3)):
        lis.append(chars[0] * 3)
        lis.append(chars[0]+chars[1])
        lis.append(chars[1]+chars[0])
        lis.append(chars[2])
        return lis
    else:
        lis.append(chars[0] * 4)
        lis.append((chars[0] * 2) + chars[1])
        lis.append(chars[1] + (chars[0] * 2))
        lis.append(chars[0] + chars[1] + chars[0])
        lis.append(chars[1] * 2)
        lis.append(chars[0] + chars[2])
        lis.append(chars[2] + chars[0])
        lis.append(chars[3])
        return lis

def display(ans):
    i = 0
    while i < len(ans) - 1:
        print(ans[i], end = ", ")
        i += 1
    print(ans[i])
main()
