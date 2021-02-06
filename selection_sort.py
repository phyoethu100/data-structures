numbers = [84, 33, 1, 49, 55, 24, 11, 98, 5, 68]

def selection_sort(array):
    length = len(array)

    for i in range(0, length):
        minimum = i
        temp = array[i]
        for j in range(i+1, length):
            if array[j] < array[minimum]:
                minimum = j
        
        array[i] = array[minimum]
        array[minimum] = temp
    return array


# Testing
print("Before sorting...")
print(numbers)
print("After sorting...")
selection_sort(numbers)
print(numbers)