print("Enter any five numbers: ")
nums = input()
num_list = nums.split(' ')

sum = 0

for i in num_list:
    sum += float(i)

print("The sum of entered numbers is ", sum)
