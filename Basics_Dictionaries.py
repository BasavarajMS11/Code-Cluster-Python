'''
Dictionaries:
Key value pairs
Associative array similar to hashmap
Dictionaries are unordered - cannot be sorted as dictionary
'''
def creating_dictionary():
    #Direct initialization
    a={'red':120,'green':0,'blue':0}
    print(a)

    #Using list of tuples
    b=dict([('red',120),('green',0),('blue',0)])
    print(b)

    #Using assignment
    c=dict(red=120,green=0,blue=0)
    print(c)

def operations_on_dict():
    #Adding or updating the value based on key
    a={'red':120,'green':0,'blue':0}
    a['white'] = 200
    a['red']=125
    print(a)

    #Deleting a key-value pair based on key
    del(a['white'])
    print(a)

    #Length of dictionary
    print(len(a))

    #Delete all items of dict
    a.clear()
    print(a)

    #Delete dict
    del(a)

def access_keys_values():
    a={'red':120,'green':0,'blue':0}
    print(a.keys())
    print(a.values())
    print(a.items())

    #Check if key exists
    print('red' in a)

    #Check if value exists
    print('red' in a.values())

def iterating_dictionary():
    a={'red':120,'green':0,'blue':0}
    for key in a:
        print(key, a[key])
    
    for key, value in a.items():
        print(key, value)

if __name__ == "__main__":
    creating_dictionary()
    print("**************************")
    operations_on_dict()
    print("**************************")
    access_keys_values()
    print("**************************")
    iterating_dictionary()