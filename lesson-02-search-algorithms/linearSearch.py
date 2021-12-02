# LINEAR SEARCH ALGORITHM

myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

def linearSearch(given_list,num):
    index = 0
    result = None
    for i in given_list:
        if i==num:
            result = index
            break
        index += 1
    return result

print(linearSearch(myList, 10))
print(linearSearch(myList, 45))
print(linearSearch(myList, 11))
print(linearSearch(myList, 100))