def berechne_indizes(test_list):
    indizes = {}
    for index, element in enumerate(test_list):
        if element in indizes:
            indizes[element].append(index)
        else:
            indizes[element] = [index]
    return indizes

test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
ergebnis = berechne_indizes(test_list)
print(ergebnis)