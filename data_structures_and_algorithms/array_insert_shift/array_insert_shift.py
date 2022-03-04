import math
def insertShiftArray(arr , n):
   mid = math.floor(len(arr)/2)
   arr = arr + [n]
   i = len(arr)
   
   while (i> mid):
       arr[i-1]=arr[i-2]
       i-=1



   arr[mid]=n
   return arr


  


print(insertShiftArray([9,8,7,6,3,2], 5))