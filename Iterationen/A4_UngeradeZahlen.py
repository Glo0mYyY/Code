count = 0
for i in range(999999):
    if count == 10:
        break
    if i % 2 == 1:
        print(i)
        count += 1
