def filter_dict_by_keys(dictionary, keys):
    new_dict = {}
    for key in keys:
        if key in dictionary:
            new_dict[key] = dictionary[key]
    return new_dict

sample_dict = { "name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
keys = ["name", "salary"]

new_dict = filter_dict_by_keys(sample_dict, keys)
print(new_dict)