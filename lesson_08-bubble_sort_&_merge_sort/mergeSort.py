def mergeSort(arr):
	if len(arr) > 1:

		mid = len(arr)//2
		L = arr[:mid]
		R = arr[mid:]

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1

		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1

		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1


array = [34, 25, 20, 5, 44, 12, 9]

print("Given array:\n", array)
mergeSort(array)
print("Sorted array:\n", array)