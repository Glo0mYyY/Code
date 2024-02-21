keys = ["ten", "twenty", "thirty"]
values = [10, 20, 30]

def mergeListe(keys, values):
    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]
    return dictionary

print(mergeListe(keys, values))