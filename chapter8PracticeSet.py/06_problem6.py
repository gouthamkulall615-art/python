def rem(l, word):
    for item in l:
        l.remove(word)
        return l


l = ["Harry", "Goutham", "Rohan", "An"]

print(rem(l, "An"))
