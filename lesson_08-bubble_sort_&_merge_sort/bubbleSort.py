def bubbleSort(arr):
    for k in range(len(arr)):
        for i in range(len(arr)-k-1):
            if arr[i]>arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

# array = [34, 25, 20, 5, 44]
array = [1100, 25, 90, 409, 367, -14, 0, -89, 900]
print(bubbleSort(array))