from functools import reduce

a = [111, 22, 65, 789, 44]


def greater(a, b):
    if a > b:
        return a
    return b


print(reduce(greater, a))
