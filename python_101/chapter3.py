# Chapter 3: Lists, Tuples, and Dictionaries
"""
# Lists
my_list = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "Python", 5]
my_nested_list = [my_list, my_list2]

print(my_list)
print(my_list2)
print(my_list3)
print(my_nested_list )

combo_list = []
one_list = [4, 5]
combo_list.extend(one_list)
print(combo_list)

combo_list2 = my_list + my_list2
print(combo_list2)

alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list)

sorted_list = alpha_list.sort()
print(sorted_list)

print(alpha_list[0:3])

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0:3])

another_tuple = tuple()
abc = tuple([1, 2, 3]) #casting a list to a tuple
print(abc)

abc_list = list(abc) #casting a tuple to a list
print(abc_list)

"""
# Dictionaries
my_dict = {}
another_dict = dict()
my_other_dict = {"one":1, "two":2, "three":3}
print(my_other_dict)
print(my_other_dict["one"])

my_dict2 = {"name":"Mike", "address":"123 Fake Street"}
print(my_dict2["name"])

print("name" in my_dict2)
print("state" in my_dict2)

print(my_dict2.keys())

