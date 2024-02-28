def find_second_largest(numbers):
    largest = 0
    second_largest = 0

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


list1 = [10, 20, 4]
print(find_second_largest(list1))

list2 = [70, 11, 20, 4, 100]
print(find_second_largest(list2))