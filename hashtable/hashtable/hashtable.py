class Hashtable(object):
    def __init__(self, size = 1024):
    
        self.size = size
        self.map = [None]*size


    def hash(self, key):
        """
        - ascii code of a key summation
        - encode chars in key into oct and add it to ascii sum
        - Prime = 19 then multiply it by ascii sum
        - mod the result over self.size
        - return the hashed value
        """
        sum_of_ascii = 0
        for ch in key:
            ch_ascii = ord(ch)
            sum_of_ascii+=ch_ascii
        hashed_key = (sum_of_ascii*19)%self.size

        return hashed_key

    def set(self, key, value):
    # def __setitem__(self, key, value):
        # get index from get_hash
        idx = self.hash(key)
        # check if the bucket at that index is empty, add the value there
        if not self.map[idx]:
            self.map[idx] = [[key, value]] # LinkedList().add({key, value})
        # if the bucker is not empty, append, add to the sotrage object(collision)
        else:
            self.map[idx].append([key, value])


    def contains(self,key):
        '''
        contains
        Arguments: key
        Returns: Boolean, indicating if the key exists in the table already.
        '''
        # call the get hash method and send the key to it 
        idx = self.hash(key)
        if (self.map[idx] != None):
            return True
        else:
            return False

    def keys(self):
        '''
        Returns: Collection of keys
        '''
        keysList = []
        for x in range(self.size):
            if (self.map[x] != None):
                for i in range(len(self.map[x])):
                    keysList.append(self.map[x][i][0])
        return keysList
    

    def get(self,key):
        '''
        Arguments: key
        Returns: Value associated with that key in the table
        '''
        if self.contains(key) == False:
            return None
        else:
            v = []
            idx = self.hash(key)
            for i in range(len(self.map[idx])):
                if (key == self.map[idx][i][0]):
                    v.append(self.map[idx][i][1])
            return ','.join(v)



if __name__ == "__main__":
    hashtable = Hashtable()
    hashtable.set("cloud", "AWS")
    hashtable.set("cloud", "Azure")
    hashtable.set("nest","pass1")
    hashtable.set("estn","pass2")
    hashtable.set("ttt", "Rainy")
    hashtable.set("name", "Python")
    print(hashtable.get("nest"))



    # for item in enumerate(hashtable.map):
    #     if item is not None:
    #         print(item)
