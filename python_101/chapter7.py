# Chapter 7 - Exception Handling
"""
try:
    1 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

my_dict = {"a": 1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("That key does not exist!")

my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list!")

print("\n")

my_dict = {"a": 1, "b":2, "c":3}
try:
    value = my_dict["d"]
except IndexError:
    print("This index does not exist!")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occured!")

try:
    value = my_dict["d"]
except (IndexError, KeyError):
    print("An IndexError or KeyError occured!")


my_dict = {"a": 1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("A KeyError occured!")
finally:
    print("The finally statement has executed!")

"""
my_dict = {"a": 1, "b":2, "c":3}
try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occured!")
else:
    print("No error occured!")
finally:
    print("The finally statement ran!")

