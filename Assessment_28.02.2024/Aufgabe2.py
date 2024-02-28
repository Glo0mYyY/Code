def filter_words_by_letter(word_list, letter):
    filtered_list = []
    for word in word_list:
        if word.startswith(letter):
            filtered_list.append(word)
    return filtered_list


word_list = ["jan", "yanis", "julian", "julius", "yannick", "jules"]
print(filter_words_by_letter(word_list, "j"))
 