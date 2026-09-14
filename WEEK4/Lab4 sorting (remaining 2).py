#G.Subramanyam
#Merge sort 
'''def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # Recursively sort the subarrays
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    # Merge the sorted subarrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    # Copy any remaining elements of left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    # Copy any remaining elements of right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1 
# Main program
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))
merge_sort(arr)
print('Sorted array:')
for element in arr:
    print(element, end=" ") '''

#G.Subramanyam
'''def quicksort(a, low, high):
    if low < high:
        # Choose the last element as pivot
        pivot = high
        i = low - 1  # Index of smaller element
        # Partition the array around the pivot
        for j in range(low, high):
            if a[j] <= a[pivot]:
                i += 1
                a[i], a[j] = a[j], a[i]  # Swap elements
        # Place the pivot in its correct position
        a[i + 1], a[pivot] = a[pivot], a[i + 1]
        pivot_index = i + 1
        # Recursively sort elements before and after partition
        quicksort(a, low, pivot_index - 1)
        quicksort(a, pivot_index + 1, high)

# Main code to take input from user
n = int(input("Enter the number of elements: "))
arr = []
print("Enter the elements:")
for _ in range(n):
    arr.append(int(input()))

# Call quicksort with proper parameters
quicksort(arr, 0, n - 1)

print('Sorted array:')
for element in arr:
    print(element, end=" ")'''
