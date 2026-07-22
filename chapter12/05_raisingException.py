a = int(input("ente a number 1:"))
b = int(input("ente a number 2:"))

if b == 0:
    raise ZeroDivisionError("Hey our program is not meant to divide numbers by zero")

else:
    print(f"The division a/b is {a/b}")
