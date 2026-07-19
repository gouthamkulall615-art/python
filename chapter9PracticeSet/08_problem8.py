with open("chapter9PracticeSet/this.txt") as f:
    content = f.read()

with open("chapter9PracticeSet/this.txt", "w") as f:
    f.write(content)
