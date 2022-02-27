
def revarray(arr):
    n = 0
    for i in arr:
        n+=1
    i=0
    n = n-1
    while(i<n):
        temp = arr[i]
        arr[i] = arr[n]
        arr[n] = temp
        i+=1  
        n-=1 
    return arr


  


print(revarray([9,8,7,6,5]))
