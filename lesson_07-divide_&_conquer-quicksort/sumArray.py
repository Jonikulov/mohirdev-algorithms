# answer with recursion
def sum_array(array):
    if array == []:
        return 0
    return array[0]+sum_array(array[1:])

array = [5, 8, 12, 22]
print(sum_array(array))