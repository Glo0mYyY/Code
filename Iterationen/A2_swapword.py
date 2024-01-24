name = "Jan"
i = len(name) - 1
reverseName = ""

while i >= 0:
    reverseName += str(name[i])
    i -= 1

print(reverseName)