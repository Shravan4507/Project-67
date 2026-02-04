def selection_sort(arr):
    """
    Sorts an array using selection sort algorithm
    """
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# Static input
numbers = [64, 25, 12, 22, 11, 90, 45, 33]

print("Original array:", numbers)
sorted_array = selection_sort(numbers.copy())
print("Sorted array:", sorted_array)
