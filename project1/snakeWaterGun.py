import random

"""
1 for snake
-1 for water
0 for gun


"""

computer = random.choice([-1, 0, 1])
youStr = input("Enter ur choice : ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youStr]
reverseDict = {1: "snake", -1: "water", 0: "gun"}

print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")


if computer == -1 and you == 1:
    print("You win!")

elif computer == -1 and you == 0:
    print("You Lose!")

elif computer == -1 and you == -1:
    print("TIE")

elif computer == 1 and you == -1:
    print("You Lose!")

elif computer == 1 and you == 0:
    print("You Win!")


elif computer == 1 and you == 1:
    print("TIE")

elif computer == 0 and you == -1:
    print("You Lose!")

elif computer == 0 and you == 1:
    print("You Lose!")


elif computer == 0 and you == 0:
    print("TIE")


else:
    print("something went wrong")
