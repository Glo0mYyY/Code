def berechne_index(test_list):
    index_list = {}
    for index, element in enumerate(test_list):
        if element in index_list:
            index_list[element].append(index)
        else:
            index_list[element] = [index]
    return index_list


test_list = [7, 6, 3, 7, 8, 3, 6, 7, 8]
print(berechne_index(test_list))
