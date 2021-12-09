# Selection Sort Algorithm

def selectionSort(array):
    sorted_list = []

    while array:
        max_item = 0

        for i in range(len(array)):
            if array[i]>array[max_item]:
                max_item = i

        sorted_list.append(array.pop(max_item))
    return sorted_list


list1 = [3, 41, 999, 5, 132,33,33,33, 6, 7, 8, 9, 34, 367, 92, 821, 281]
print(selectionSort(list1))