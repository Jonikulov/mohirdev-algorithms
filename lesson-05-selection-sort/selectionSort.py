# Selection Sort Algorithm

def selectionSort(array):
    sorted_list = []

    while array:
        max_item = array[0]
        for k in array:
            if k>max_item:
                max_item = k
        sorted_list.append(max_item)
        # need an improvement
        array.remove(max_item)
    return sorted_list

list1 = [3, 41, 999, 5, 132,33,33,33, 6, 7, 8, 9, 34, 367, 92, 821, 281]

print(selectionSort(list1))