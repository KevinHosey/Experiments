# Chapter 5 - Loops
"""
for number in range(5):
    print(number)


a_dict = {"one":1, "two":2, "three":3}
for key in a_dict:
    print(key)

a_dict = {1:"one", 2:"two", 3:"three"}
keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)

for number in range(10):
    if number % 2 == 0:
        print(number)


i = 0
while i < 10:
    print(i)
    i = i + 1

j = 0
while j < 10:
    print (j)
    if j == 5:
        break
    j +=1

i = 0
while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1
"""
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    if i == 7:
        print("Item found!")
        break
    print(i)
else:
    print("Item not found!")
