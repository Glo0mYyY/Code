listA = [1, 2, 3, 4, 5]
listB = [8, 9, 10, 6, 7]
sameValue = False

for num in listA:
    if num in listB:
        sameValue = True

if sameValue:
    print("There are same values in both lists.")
else:    
    print("There are no same values in both lists.")