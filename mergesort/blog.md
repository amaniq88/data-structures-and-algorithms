# MergeSort
 Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves, and then it merges the two sorted halves. 
## Pseudocode

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

## Trace
Sample Array: [8,4,23,42,16,15]
n= 6 
mid = 3
left = [8,4,23]
right = [42,16,15]
===>  call the mergsort function for the left ... 
arr = [8,4,23]
n = 3 
mid = 1
left = [8]
right = [4, 23]
===>  call the mergsort function for the left ... In this Case the len(left) is One so skip 
and check for the right array 
arr = [4, 23]
mid = 1 
left = [4]
right = [23]

===>  call the Merge function for Merge([4],[23],arr)
i , j , k = 0
compair the value of left (4 <? 23) -- CORRECT
arr[0] = 4
i = 1
k = 1
arr[1]= 23
i = 2
j = 1

arr= [4, 23]

**Pass 2:**
back to merge CALL ON left ( left = [8]  ) 
merge([4, 23] , [8], arr )
if 4 < 8 --- CORRECT 
arr[0] = 4
i = 1
k = 1

if 23 < 8  ... X 
arr[1] = 8

check for the other elemnts 
arr[2] = 23


arr = [4,8,23]
**Pass 3:**
Back to the call of merge to (right = [42,16,15])
n = 3 
mid = 1
left = [42]
right = [16, 15]
===>  call the mergsort function for the left ... In this Case the len(left) is One so skip 
and check for the right array 
arr = [16, 15]
mid = 1 
left = [16]
right = [15]

===>  call the Merge function for Merge([16],[15],arr)
i , j , k = 0
compair the value of left (16 <? 15) -- X
arr[0] = 15
j = 1
k = 1
arr[1]= 16
i = 1

arr= [15, 16]

**Pass 4:**

back to merge CALL ON left ( left = [42]  ) 
merge([15, 16] , [42], arr )
if 15 < 42 --- CORRECT 
arr[0] = 15
i = 1
k = 1

if 16 < 42  ... CORRECT 
arr[1] = 16

check for the other elemnts 
arr[2] = 42


arr = [15,16,42]

**Pass 5:**
Call the merge for ([4,8,23] , [15,16,42], arr )

i , j , k = 0
len(left) = 3
len(right) = 3
while (i,j < 3)
if 4 <?  15  ... CORRECT 
arr[0] = 4

i = 1 
k = 1
while (i,j < 3)
8 < 15 ... CORRECT
arr[1] = 8
i = 2
k = 2

while (i,j < 3)
23 <? 15  ... X
arr[2] = 15
j = 1
k = 3

while (i,j < 3)
23 <?16 .... X
arr[3] = 16
j = 2
k = 4

while (i,j < 3)

23 <? 42 ... CORRECT 
arr[4] = 23
j = 3
k = 5


==> check for the other item 
arr[5] = 42

sorrted array = [4, 8, 15, 16, 23, 42]






### Illustrations:
![Illustrations](pic1.jpg)

Efficency
Time Complexity: Sorting arrays on different machines. Merge Sort is a recursive algorithm and time complexity can be expressed as following recurrence relation. 
T(n) = 2T(n/2) + θ(n)

Auxiliary Space: O(n)