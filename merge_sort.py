numbers = [84, 33, 1, 49, 55, 24, 11, 98, 5, 68]


def merge_sort(array):
    length = len(array)
    if length == 1:
        return array

    mid = length // 2
    left = array[:mid]
    right = array[mid:]
  #  print(f"Left: {left}")
   # print(f"Right: {right}")
    
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    return result + left[left_index:] + right[right_index:]



# Testing
print("Before sorting...")
print(numbers)
print("After sorting...")
print(merge_sort(numbers))