#1. linear search
def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = [10, 20, 30, 40, 50,60,70]
key = int(input("enter the required value:"));
          
result = linear_search(arr, key)

if result != -1:
    print( key ,"found at index" ,result)
else:
    print("Element not found")
#2.binary search
    def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

if arr != sorted(arr):
    print("The given array is NOT sorted.")
    print("Binary search cannot be performed on an unsorted array.")
else:
    key = int(input("Enter the element to search: "))
    result = binary_search(arr, key)

    if result != -1:
        print("Element found at index", result)
    else:
        print("Element not found")
             

