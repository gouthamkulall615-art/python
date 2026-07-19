import random


def game():
    print("your are playing the game...")
    score = random.randint(1, 62)
    with open("chapter9PracticeSet/hiscore.txt") as f:
        hiscore = f.read()
        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"your score :{score}")

    if score > hiscore or hiscore == "":
        with open("chapter9PracticeSet/hiscore.txt", "w") as f:
            f.write(str(score))

    return score


game()
