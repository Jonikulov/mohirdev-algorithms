def selectionSort(array):
    sorted_list = []

    while array:
        max_item = 0
        for i in range(len(array)):
            if array[i]>array[max_item]:
                max_item = i
        sorted_list.append(array.pop(max_item))
    return sorted_list

def quickSort(arr):
    if len(arr)<2:
        return arr
    else:
        return


list1 = [3, 41, 999, 5, 132, 33, 33, 33, 6, 7, 8, 9, 34, 367, 92, 821, 281]
print(selectionSort(list1))

from random import randrange

def qsort(array):
    if len(array) < 2:
        return array
    else:
        # pivot = array.pop(0)
        pivot = array.pop(randrange(len(array)))
        kichik = [i for i in array if i <= pivot]
        katta = [i for i in array if i > pivot]
        # print(f"{kichik}+[{pivot}]+{katta}")
        return qsort(kichik) + [pivot] + qsort(katta)

if __name__ == '__main__':
    array1 = [1, 5, 12, 0, -5, 66]
    print(array1)
    print(qsort(array1))
    array2 = list(range(20))
    print(array2)
    print(qsort(array2))
    array3 = ['olma', 'anjir', 'shaftoli', 'qovun', 'tarvuz']
    print(array3)
    print(qsort(array3))
