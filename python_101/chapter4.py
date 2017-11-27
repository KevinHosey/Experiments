# Chapter 4 - Conditional Statements
"""
value = input("How much is that doggy in the window? ")
value = int(value)

if value < 10:
    print("That's a great deal!")
elif 10 <= value <= 20:
    print("I'd still pay that...")
else:
    print("Wow! That's too much!")


# Boolean Operations
x = 10
y = 20
if x < 10 or y > 15:
    print("This statement was True!")


x = 10
y = 10
if x == 10 and y == 15:
    print("This statement was True!")
else:
    print("This statement was False!")


my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print("'x' is not in the list, so this is True!")

x = 10
if x != 11:
    print("x is not equal to 11!")

"""

# Check for Nothing

empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None

if empty_list == []:
    print("It's an empty list!")

if empty_tuple:
    print("It's not an empty tuple!")

if not empty_string:
    print("This is an empty string!")

if not nothing:
    print("Then it's nothing!")



if __name__ == "__main__":
    print("Do something!")

