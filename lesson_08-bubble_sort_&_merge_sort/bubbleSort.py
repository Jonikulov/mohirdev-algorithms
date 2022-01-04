def bubbleSort(arr):
    N = len(arr)
    for k in range(N):
        for i in range(N-k-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

array1 = [34, 25, 20, 5, 44]
array2 = [100, 25, 90, 409, 367, -14, 0, -89, 900]

print(bubbleSort(array1))
print(bubbleSort(array2))