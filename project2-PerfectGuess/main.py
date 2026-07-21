import random

computer = random.randint(1, 10)

count = 0
while True:
    user = int(input("Enter ur guess(1-10)"))
    count += 1

    if user == computer:
        print("The guess is correct!")

        break

    elif user > computer:
        print("Guess a lower number.")

    else:
        print("Guess a higher number.")


print(f"Congratulations! You guessed it in {count} guesses.")
