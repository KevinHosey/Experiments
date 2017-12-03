# Chapter 8 - Working with Files
"""
handle = open("test.txt", "r")
data = handle.read()
print(data)
handle.close()

handle = open("test.txt", "r")
data = handle.readlines()
print(data)
handle.close()

handle = open("test.txt", "r")
for line in handle:
    print(line)

handle.close()

handle = open("test.txt", "r")
while True:
    data = handle.read(1024)
    print(data)
    if not data:
        break

handle = open("test.txt", "rb") # read binary file


handle = open("output.txt", "w")
handle.write("This is a test!")
handle.close()

with open("test.txt") as file_handler:
    for line in file_handler:
        print(line)

try:
    file_handler = open("test.txt")
    for line in file_handler:
        print(line)
except IOError:
    print("An IOError has occured!")
finally:
    file_handler.close()
"""
try:
    with open("test.txt") as file_handler:
        for line in file_handler:
            print(line)
except IOError:
    print("An IOError has occured!")
