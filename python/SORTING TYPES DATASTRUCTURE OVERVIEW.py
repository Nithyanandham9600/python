#BUBBLE SORT 

arr = [5, 2, 4, 1]
n = len(arr)
for i in range(n):
	for j in range(0, n-i-1):
		if arr[j] > arr[j+1]:
			arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)


# QUICK SORT 

def quicksort(arr):
	if len(arr) <= 1:
		return arr
	pivot = arr[0]
	left = [x for x in arr[1:] if x < pivot]
	right = [x for x in arr[1:] if x >= pivot]
	return quicksort(left) + [pivot] + quicksort(right)
print(quicksort([5, 3, 8, 2]))

# MERGE SORT 

def merge_sort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		L = arr[:mid]
		R = arr[mid:]

		merge_sort(L)
		merge_sort(R)

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

arr = [12, 11, 13, 5]
merge_sort(arr)
print(arr)


# INSERTION SORT 

arr = [5, 2, 4, 1]
for i in range(1, len(arr)):
	key = arr[i]
	j = i - 1
	while j >= 0 and key < arr[j]:
		arr[j + 1] = arr[j]
		j -= 1
	arr[j + 1] = key
print(arr)

# SELECTION SORT 

arr = [64, 25, 12, 22, 11]
for i in range(len(arr)):
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[min_idx] > arr[j]:
			min_idx = j
	arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)