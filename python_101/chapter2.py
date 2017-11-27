# Chapter 2: All About Strings
"""
myString = "I'm a Python programmer!"
otherString = "The word 'python' usually refers to a snake."
tripleString = 'Here's another way to embed "quotes" in a string.'

print(myString)
print(otherString)
print(tripleString)

my_number = 123
my_string = str(my_number)
print(my_string)

my_string2 = "abc"
print(id(my_string2))
my_string2 = "def"
print(id(my_string2))
my_string2 = my_string2 + "ghi"
print(id(my_string2))

my_string3 = "This is string!"
print(my_string3.upper())

my_string = "I like Python!"
print(my_string[0:1])
print(my_string[2:])
print(my_string[:-5])

my_string2 = "I like %s" % "coding in Python"
print(my_string2)
var = "cookies"
new_string = "I like %s" % var
print(new_string)
another_string = "I like %s and %s" % ("Python", var)
print(another_string)

int_string = "%i + %i = %i" % (1, 2, 3)
print(int_string)
float_string = "%f" % (1.23)
print(float_string)
float_string2 = "%.2f" % (1.23)
print(float_string2)
"""

print("%(lang)s is fun!" % {"lang": "Python"})
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})
print("%(x)i + %(y)i = %(z)i" % {"x":1, "y":2, "z":3})

print("Python is as simple as {0}, {1}, {2}".format("a", "b", "c"))
print("Python is as simple as {1}, {0}, {2}".format("a", "b", "c"))
xy = {"x":0, "y":10}
print("Graph a point at where x={x} and y={y}".format(**xy))
