# it is  an immutable datatype
# Creating a tuple
t = (10, 20, 30, 20, 40)

# ---------------------------------------
# 1. count(value)
# Returns the number of times the value appears in the tuple.
# ---------------------------------------
print(t.count(20))     # Output: 2

# ---------------------------------------
# 2. index(value)
# Returns the index of the first occurrence of the value.
# Raises ValueError if the value is not found.
# ---------------------------------------
print(t.index(30))     # Output: 2


t = (10, 20, 30, 40, 50)

# ---------------------------------------
# len(tuple)
# Returns the number of elements.
# ---------------------------------------
print(len(t))          # Output: 5

# ---------------------------------------
# max(tuple)
# Returns the largest element.
# ---------------------------------------
print(max(t))          # Output: 50

# ---------------------------------------
# min(tuple)
# Returns the smallest element.
# ---------------------------------------
print(min(t))          # Output: 10

# ---------------------------------------
# sum(tuple)
# Returns the sum of all numeric elements.
# ---------------------------------------
print(sum(t))          # Output: 150

# ---------------------------------------
# sorted(tuple)
# Returns a sorted LIST (not a tuple).
# ---------------------------------------
print(sorted(t, reverse=True))
# Output: [50, 40, 30, 20, 10]

# ---------------------------------------
# tuple(iterable)
# Converts an iterable into a tuple.
# ---------------------------------------
lst = [1, 2, 3]
new_tuple = tuple(lst)
print(new_tuple)       # Output: (1, 2, 3)

# ---------------------------------------
# any(tuple)
# Returns True if at least one element is True.
# ---------------------------------------
print(any((0, False, 5)))      # Output: True

# ---------------------------------------
# all(tuple)
# Returns True only if all elements are True.
# ---------------------------------------
print(all((1, True, 5)))       # Output: True
print(all((1, 0, 5)))          # Output: False


t1 = (1, 2, 3)
t2 = (4, 5, 6)

# ---------------------------------------
# Concatenation (+)
# Joins two tuples.
# ---------------------------------------
print(t1 + t2)
# Output: (1, 2, 3, 4, 5, 6)

# ---------------------------------------
# Repetition (*)
# Repeats the tuple.
# ---------------------------------------
print(t1 * 3)
# Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# ---------------------------------------
# Membership (in / not in)
# Checks whether an element exists.
# ---------------------------------------
print(2 in t1)         # Output: True
print(7 not in t1)     # Output: True

# ---------------------------------------
# Slicing
# Returns a portion of the tuple.
# ---------------------------------------
print(t2[1:])          # Output: (5, 6)

# ---------------------------------------
# Unpacking
# Assigns tuple elements to variables.
# ---------------------------------------
a, b, c = t1
print(a, b, c)         # Output: 1 2 3