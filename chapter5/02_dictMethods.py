marks={
    "Harry":100,
    "Goutham":55,
    "Rohan":23
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99,"Preethu":100})
# print(marks)

# print(marks.get("Harry2")) #here if the harry 2 doesnt exist then it will show none
# print(marks["Harry2"])# here it shows the erro

# removed = marks.pop("Goutham")
# print(removed)

removed = marks.popitem()

print(removed)
print(marks)