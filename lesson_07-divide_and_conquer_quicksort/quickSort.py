from random import randrange

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr.pop(randrange(len(arr)))
        low = [i for i in arr if i<=pivot]
        high = [i for i in arr if i>pivot]
        return quickSort(low) + [pivot] + quickSort(high)


array = [3, 41, 999, 5, 132, 33, 33, 33, 6, 7, 8, 9, 34, 367, 92, 821, 281]
print(quickSort(array))