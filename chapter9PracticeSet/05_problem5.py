words = ["Donkey", "bad", "ganda"]

with open("chapter9PracticeSet/file.txt", "r") as f:
    content = f.read()
    for word in words:
        content = content.replace(word, "#" * len(word))


with open("chapter9PracticeSet/file.txt", "w") as f:
    f.write(content)
