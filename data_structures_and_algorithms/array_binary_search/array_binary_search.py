def BinarySearch(sortedarr, x):
    low = 0
    high = len(sortedarr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if sortedarr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif sortedarr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1

# Test array
arr = [ 10, 20, 30, 40, 50 ]
x = 50

# Function call

print(BinarySearch(arr, x))

