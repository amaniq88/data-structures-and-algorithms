# Python program for implementation of Insertion Sort



from logging import exception


def insertionSort(arr):


	# Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        if (type(key) == str):
            raise Exception("value Error")

		# Move elements of arr[0..i-1], that are
		# greater than key, to one position ahead
		# of their current position
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
