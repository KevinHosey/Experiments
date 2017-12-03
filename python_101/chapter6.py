# Chapter 6 - Python Comprehensions
"""
# List comprehensions
x = [i for i in range(5)]
print(x)

x = ['1', '2', '3', '4', '5']
y = [int(i) for i in x]
print(y)

myStringsList = ["I   ", " got ", "a ", "    name"]
myStrings = [s.strip() for s in myStringsList]
for x in myStrings:
    print(x)

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])


# Dictionary comprehensions
print ( {i: str(i) for i in range(5)} )

my_dict = {1: "dog", 2:"cat", 3:"hamster"}
print( {value:key for key, value in my_dict.items()} )

"""
# Set comprehensions
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
print(my_set)

my_set2 = {x for x in my_list}
print(my_set2)
