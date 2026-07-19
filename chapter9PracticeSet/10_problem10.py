with open("chapter9PracticeSet/old.txt") as f:
    content = f.read()
with open("chapter9PracticeSet/renamed_by_python.txt", "w") as f:
    f.write(content)
