# Hashtables
A hash is the result of some algorithm taking an incoming string and converting it into a value that could be used for either security or some other purpose. In the case of a hashtable, it is used to determine the index of the array. Buckets - A bucket is what is contained in each index of the array of the hashtable. Each index is a bucket. An index could potentially contain multiple key/value pairs if a collision occurs. Collisions - A collision is what happens when more than one key gets hashed to the same location of the hashtable.


## Challenge
implemntation for the Hashtable Class and add the below methods : 
set / get / hash /key /contains 

## Approach & Efficiency
for the Hash method take each char in the key and convert to ASCI code then find the summiation .
for the set save the key , value pair as list of list ( to solve the collision case) inside the list 
get / key / contain : using normal loop /IF statment to check for these methods 

## API
- set
Arguments: key, value
Returns: nothing
This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
Should a given key already exist, replace its value from the value argument given to this method.
- get
Arguments: key
Returns: Value associated with that key in the table
- contains
Arguments: key
Returns: Boolean, indicating if the key exists in the table already.
- keys
Returns: Collection of keys
- hash
Arguments: key
Returns: Index in the collection for that key