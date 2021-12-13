# BINARY SEARCH ALGORITHM

def binarySearch(given_list,item):
    low = 0
    high = len(given_list)-1
    while low<=high:
        mid = low+high//2
        if given_list[mid]==item:
            return mid
        elif given_list[mid]<item:
            low = mid+1
        else:
            high = mid-1
    return None


myList = [1,3,4,6,7,8,10,12,23,45,56,78,99]

print(binarySearch(myList, 10))
print(binarySearch(myList, 45))
print(binarySearch(myList, 11))
print(binarySearch(myList, 100))
print(binarySearch(myList, 99))