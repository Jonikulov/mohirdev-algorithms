def bubbleSort(arr):
    N = len(arr)
    for k in range(N):
        for i in range(N-k-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

# array = [34, 25, 20, 5, 44]
array = [100, 25, 90, 409, 367, -14, 0, -89, 900]

print("Given array:\n", array)
bubbleSort(array)
print("Sorted array:\n", array)
