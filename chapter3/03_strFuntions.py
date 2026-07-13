# ==========================
# Python String Functions
# ==========================

s = "  Hello World  "

# 1. Length of string
print(len(s))                 # 15

# 2. Convert to lowercase
print(s.lower())              # "  hello world  "

# 3. Convert to uppercase
print(s.upper())              # "  HELLO WORLD  "

# 4. Capitalize first letter
print(s.capitalize())         # "  hello world  "

# 5. Title case
print(s.title())              # "  Hello World  "

# 6. Swap uppercase <-> lowercase
print(s.swapcase())           # "  hELLO wORLD  "

# 7. Remove spaces from both ends
print(s.strip())              # "Hello World"

# 8. Remove spaces from left
print(s.lstrip())             # "Hello World  "

# 9. Remove spaces from right
print(s.rstrip())             # "  Hello World"

# 10. Replace substring
print(s.replace("World", "Python"))   # "  Hello Python  "

# 11. Split string into list
print(s.split())              # ['Hello', 'World']
print("a,b,c".split(","))     # ['a', 'b', 'c']

# 12. Join list into string
words = ["Hello", "World"]
print(" ".join(words))        # "Hello World"

# 13. Find first occurrence
print(s.find("World"))        # 8
print(s.find("Python"))       # -1

# 14. Index of substring (throws error if not found)
print(s.index("World"))       # 8

# 15. Count occurrences
print("banana".count("a"))    # 3

# 16. Starts with
print(s.startswith("  He"))   # True

# 17. Ends with
print(s.endswith("  "))       # True

# 18. Check if all letters
print("Hello".isalpha())      # True
print("Hello1".isalpha())     # False

# 19. Check if all digits
print("12345".isdigit())      # True

# 20. Check if alphanumeric
print("abc123".isalnum())     # True

# 21. Check if lowercase
print("hello".islower())      # True

# 22. Check if uppercase
print("HELLO".isupper())      # True

# 23. Check if whitespace
print("   ".isspace())        # True

# 24. Check if title case
print("Hello World".istitle())    # True

# 25. Center align
print("Hi".center(10, '-'))   # "----Hi----"

# 26. Left justify
print("Hi".ljust(10, '-'))    # "Hi--------"

# 27. Right justify
print("Hi".rjust(10, '-'))    # "--------Hi"

# 28. Zero fill
print("42".zfill(5))          # "00042"

# 29. Partition
print("apple-banana".partition("-"))
# ('apple', '-', 'banana')

# 30. Reverse partition
print("apple-banana".rpartition("-"))
# ('apple', '-', 'banana')

# 31. Encode string
print("Hello".encode())       # b'Hello'

# 32. Remove prefix (Python 3.9+)
print("unhappy".removeprefix("un"))    # "happy"

# 33. Remove suffix (Python 3.9+)
print("filename.txt".removesuffix(".txt"))   # "filename"

# 34. Case-insensitive comparison
print("hello".casefold())     # "hello"