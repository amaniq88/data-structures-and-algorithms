class Cat :
    '''
    Cat Class 
    '''
    def __init__(self,value):
        self.value = value 
        self.next = None

class Dog :
    '''
    dog Class
    '''
    def __init__(self,value):
        self.value = value 
        self.next = None

class AnimalShelter:
    '''
    First-in, First out Animal Shelter.
    '''
    def __init__(self):
        self.front  = None
        self.rear = None

    def __str__(self):
        '''
        this method is used to printout the Animal Shelters 
        '''
        output = ""
        if self.front is None:
            output = "Empty Queue !"
        else:
            current = self.front
            while(current):
                output+= f'{[current.value]} -> '
                current = current.next
            
        return output
    def enqueue(self, animal):
        '''
        Arguments: animal
        animal can be either a dog or a cat object.
        '''
        if (animal == "dog"):
            animal = Dog(animal)
        elif ( animal == "cat"):
            animal = Cat(animal)
        else :
            raise Exception("value should by  animal only Dog / Cat")

        if not self.front:
            self.rear = animal
            self.front = animal
        else:
            self.rear.next = animal 
            self.rear = animal 


    def dequeue(self, pref):
        '''
        dequeue
        Arguments: pref
        pref can be either "dog" or "cat"
        Return: either a dog or a cat, based on preference.
        If pref is not "dog" or "cat" then return null.
        '''
        if (self.front == None):
            raise Exception("The shelter is empty")
        elif (self.front.value == pref):
                temp = self.front
                self.front = self.front.next
                temp.next = None
                return temp.value
        elif ((pref == "dog") or  (pref == "cat")) :
                previouAnimal = None
                prefPosition = self.front
                while(prefPosition):
                    if (prefPosition.value == pref):
                        temp = prefPosition.next
                        previouAnimal.next = temp 
                        return prefPosition.value
                    previouAnimal =  prefPosition
                    prefPosition = prefPosition.next
        else:
                return None


if __name__ == "__main__":
    pass


        

