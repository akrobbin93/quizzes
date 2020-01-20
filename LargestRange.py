#----------------------------------------
#LargestRange.py
#Author: akrobbin93
#Quiz: Given an array of ints, find the
#largest range, return array
#of [smallest, largest]
#----------------------------------------

def LargestRange(array):
    list_of_numbers = {x:0 for x in array}
    left = right = 0

    for current_number in array:
        if list_of_numbers[current_number] == 0:
            left_count = current_number - 1
            right_count = current_number + 1

            while left_count in list_of_numbers:
                list_of_numbers[left_count] = 1
                left_count -= 1
            left_count += 1

            while right_count in list_of_numbers:
                list_of_numbers[right_count] = 1
                right_count += 1
            right_count -= 1

            if(right - left) <= (right_count - left_count):
                right = right_count
                left = left_count
    return [left, right]


    return
#----------------------------------------

test_array = [1, 2, 3, 4, 5, 6]
print(LargestRange(test_array))

test_array = [2, 1, 5, 4, 3, 6]
print(LargestRange(test_array))

test_array = [11, 10, 7, 8, 15, 6, 16]
print(LargestRange(test_array))
