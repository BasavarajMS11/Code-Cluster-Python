'''
Sets:
Store non duplicate items
Very fast access against lists
Math set operations - Union, Intersection
Sets are unordered
'''
def creating_sets():
    #Duplicate items
    a={1,2,2,3}
    print(a)

    #Empty set
    b=set()
    print(b)

    #From list
    list1=[1,2,3]
    c=set(list1)
    print(c)

def operations_on_set():
    a={1,2,3}
    print(a)

    #Adding
    a.add(5)
    print(a)

    #Removing element from set
    a.remove(2)

    #Length of set
    print(len(a))

    #Check if an element is in set
    print(3 in a)

    #pop out random itwm from set
    print(a.pop(),a)

    #delete all elements
    a.clear()
    print(a)

def set_operations():
    #Let sets A and B
    A={1,2,3,4}
    B={2,4,6,8}
    #Intersection - AND ( A & B)
    print(A&B)

    #Union - OR ( A | B )
    print(A|B)

    #Symmetric Difference - XOR ( A ^ B ) in A but not in B
    print(A^B)

    #Subset - A <= B (B contains A)
    print(A<=B)

    #Superset - A >= B (A contains B)
    print(A>=B)

if __name__ == "__main__":
    print("**************************")
    creating_sets()
    print("**************************")
    operations_on_set()
    print("**************************")
    set_operations()
    print("**************************")