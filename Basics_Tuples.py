'''
Tuples:
Are immutable - can't add/change (but member objects are mutable)
Useful for fixed data
Faster than lists
Sequence types - General functions can be used
                 delete, append, insert, remove, reverse etc
'''
def creating_tuples():
    #Empty tuple
    a=()
    print(a, type(a))

    #Initializing values
    a=(1,2,3)
    print(a, type(a))

    #without paranthesis
    a=1,2,3
    a=1,
    print(a, type(a))

    #from list
    list1=[10,20,30]
    b=tuple(list1)
    print(b,type(b))

def deleting_object_elements():
    a=(1,2,3)
    #del(a[2]) #Fails since tuples are immutable
    print(a)

    #delete element from first object of tuple
    b=([1,2,3],4)
    del(b[0][2])
    print(b)

    #concatenating tuple with new one
    c=([1,2],3)
    c+=(4,)
    print(c)


if __name__ == "__main__":
    print("1.Creating Tuples------------------------------------")
    creating_tuples()
    print("2. Deleting tuple object elements------------------------------------")
    deleting_object_elements()
