def divisble5(n):
    if n % 5 == 0:
        return True
    return False


a = [1, 2, 33, 49, 455, 67, 9]


f = list(filter(divisble5, a))
print(f)
