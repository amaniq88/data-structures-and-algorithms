def mergeSort(arr):
    if len(arr) > 1:

		# Finding the mid of the array
        n = len (arr)
        mid = n//2

		# Dividing the array elements
        left = arr[:mid]

		# into 2 halves
        right = arr[mid:]

		# Sorting the first half
        mergeSort(left)

		# Sorting the second half
        mergeSort(right)

        merge(left, right, arr)



def merge(left, right, arr):
    
    i = j = k = 0

		# Copy data to temp arrays L[] and R[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

	# Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    print (arr)

arr = [8,4,23,42,16,15]
mergeSort(arr)
