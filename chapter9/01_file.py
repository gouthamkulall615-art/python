"""
The random-access memory is volatile, and all its contents are lost once a program
terminates in order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the flle by reading
content from it and writing content to it.
"""

f = open("chapter9/file.txt", "r")
data = f.read()
print(data)
f.close()
