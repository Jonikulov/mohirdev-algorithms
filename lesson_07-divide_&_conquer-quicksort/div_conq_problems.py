def len_array(array):
    """returns the number of array elements"""
    if array==[]:
        return 0
    return 1+len_array(array[1:])

def max_array(array):
    """returns the largest element of an array"""
    if array==[]:
        return 0
    else:
        A = max_array(array[1:])
        return A if A > array[0] else array[0]

def binary_search_recursive(arr, elem, start=0, end=None):
    if end == None:
        end = len(arr) - 1
    if start > end:
        return None

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binary_search_recursive(arr, elem, start, mid-1)
    # elem > arr[mid]
    return binary_search_recursive(arr, elem, mid+1, end)


array = [2,4,5,6,8,9,10,11,12,15,25,37,40]

print("array length:", len_array(array))
print("max element in array:", max_array(array))
print("element index:", binary_search_recursive(array, 12))
print("element index:", binary_search_recursive(array, 120))