numberList = [1, 5, 3, 9, 3, 5, 3, 8, 9, 7]
newList = []

for num in numberList:
    if num not in newList:
        newList.append(num)

print(newList)
