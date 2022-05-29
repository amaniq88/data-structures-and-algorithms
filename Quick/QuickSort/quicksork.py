def partition(array, low, high):
    # Choose the rightmost element as pivot
    pivot = array[high]
    # Pointer for greater elementz
    i = low - 1
    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        print (array)
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1

    # Function to perform quicksort
def quick_sort(array, low, high):
    for h in range(len(array)):
        if (type(array[h]) == str):
            raise Exception("value Error")
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)
    return array

