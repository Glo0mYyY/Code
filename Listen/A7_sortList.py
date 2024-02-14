randomNumbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4]
for i in range(len(randomNumbers)):
    index1 = i
    index2 = i + 1
    if index2 == len(randomNumbers)-1:
        break
    for j in range(len(randomNumbers)):
        if randomNumbers[index1] > randomNumbers[index2]:
            memory = randomNumbers[index2]
            randomNumbers[index2] = randomNumbers[index1]
            randomNumbers[index1] = memory
        index2 += 1
        if index2 == len(randomNumbers):
            break
            print (index2)
print (randomNumbers)