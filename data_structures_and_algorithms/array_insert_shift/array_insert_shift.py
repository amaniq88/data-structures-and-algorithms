import math
def insertShiftArray(arr , n):
   mid = math.floor(len(arr)/2)
   arr = arr[0:mid] + [n] + arr[mid:]  
   return arr


  


print(insertShiftArray([9,8,7,6], 5))