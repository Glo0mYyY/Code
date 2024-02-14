i = 0
count = 0
while True:
    if count == 10:
        break
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    count += 1
