def group_elements(list):
    result_dictionary = {}
    for element in list:
        if element in result_dictionary:
            result_dictionary[element].append(element)
        else:
            result_dictionary[element] = [element]
    return result_dictionary


list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
print(group_elements(list))
