f = open("chapter9/file.txt")
print(f.read())
f.close()

# the same can be written using statement like this:

with open("chapter9/file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file
