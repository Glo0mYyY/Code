def find_least_common_char_frequency(string):
    char_frequency = {}
    
    for char in string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    
    least_common_char = None
    least_common_frequency = float("inf")
    
    for char, frequency in char_frequency.items():
        if frequency < least_common_frequency:
            least_common_char = char
            least_common_frequency = frequency
    
    return least_common_frequency

string = "dasisteintestdasisteintest"
least_common_frequency = find_least_common_char_frequency(string)
print("Die Häufigkeit des am wenigsten vorkommenden Zeichens in ", string, "ist ",  least_common_frequency)
