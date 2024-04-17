# exercise:
# 1. find the number of items in a list
# 2. find the sum of the items in a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
sum = 0

for number in my_list:
    count += 1
    sum += number

print(count)
print(sum)
