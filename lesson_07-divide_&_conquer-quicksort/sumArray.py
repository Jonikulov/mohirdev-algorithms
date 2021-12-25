def sum_array(array):
    index = 0
    if array[index]!=array[-1]:
        return array[index+1]+sum_array(array[index+1:])
        # index += 1
    #     pass
    # else:


array = [5, 8, 12, 22]
print(sum_array(array))