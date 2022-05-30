from hashmap_left_join.hashtable import Hashtable
def leftjoin(Hash1, Hash2):
    '''
    LEFT JOIN for 2 Hashmaps
    Input : Two Hash map Object 
    Output : Joined list
    '''
    output = []
    # check for Edge Cases Not valid Input 
    try:
        Hash1.keys()
    except AttributeError:
        raise Exception

    for i in Hash1.keys():
        hashitem = []
        if Hash2.contains(i):
            hashitem.append(i)
            hashitem.append(Hash1.get(i))
            hashitem.append(Hash2.get(i))
        else:
            hashitem.append(i)
            hashitem.append(Hash1.get(i))
            hashitem.append(None)

        output.append(hashitem)
    return output




