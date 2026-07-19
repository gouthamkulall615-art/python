word = "Donkey"

with open("chapter9PracticeSet/file.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "######")

with open("chapter9PracticeSet/file.txt", "w") as f:
    f.write(contentNew)
