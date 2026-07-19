with open("chapter9PracticeSet/file1.txt") as f:
    content1 = f.read()
with open("chapter9PracticeSet/file2.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("yes these files are identical")

else:
    print("NO these files are not identical")
