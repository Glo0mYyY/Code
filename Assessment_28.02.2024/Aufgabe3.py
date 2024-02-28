def find_least_common_char_frequency(string):
    char_frequency = {}

    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    least_common_char = None
    least_common_frequency = 0

    for char, frequency in char_frequency.items():
        if frequency < least_common_frequency or least_common_frequency == 0:
            least_common_char = char
            least_common_frequency = frequency

    return ("char", char, "frequency", least_common_frequency)


string = "dasisteintestdasisteintest"
print(find_least_common_char_frequency(string))
