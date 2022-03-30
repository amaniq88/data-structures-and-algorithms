# Challenge Summary
First-in, First out Animal Shelter.
for Only two kinds of animals ( Cats /  Dogs )
## Whiteboard Process
![whiteboard](/stack_queue_animal_shelter/Challenge12.jpg)

## Approach & Efficiency
for the enqueue use O(1) for Time and Space its just add new dog/Cat instance to the reare of the queue .
for dequeue  use O(n) loop through animals till find the pref animal

## Solution
1- for enqueu  will add the animals direct to rare of queue
2- for dequeue will  do multiple check :
  1- if front eqal none means  the queue is empty rais exception .
 2- if the prefrenced eqal the front   will drect remove the front animals means change the front to the next and make it point to Null .
  3- if  the preference some where in the queue will first loop through the queue and each time save the value of previous  animal then when find make the previour point to the next of the current.
 4- else if  the value not preff return None
