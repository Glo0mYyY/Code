def group_elements(list):
    result_dict = {}
    for element in list:
        if element in result_dict:
            result_dict[element].append(element)
        else:
            result_dict[element] = [element]
    return result_dict

list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
result = group_elements(list)
print(result)