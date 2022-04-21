#Lists

def create_list():
    #Creating empty list
    a=list()
    print(a)

    #Creating by initializing
    b=['blue',255,'sky',2.0]
    print(b)

    #Creation of list using tuples
    c=(5,3)
    d=list(c)
    print(d)

    #List comprehension
    e=[ i for i in range(10)]
    print(e)
    f=[i**2 for i in range(15) if i>3]
    print(f)

def deleting():
    a=[1,2,3,4]
    #delete an element
    del(a[1])
    print(a)

    #delete entire list
    del(a)
    #print(a)

def appending():
    a=[1,2,3,4]
    a.append(5)
    print(a)

def extending():
    a=[1,3,5,7]
    b=[2,4,6,8]
    a.extend(b)
    print(a)

def inserting():
    a=[1,3,4,5]
    a.insert(1,2)
    print(a)
    a.insert(1,['two','was missing'])
    print(a)

def popout():
    a=[1,2,3,4,5]
    print(a.pop())
    print(a)

def removing():
    #removes first occurence
    a=[1,2,3,2,1]
    a.remove(2)
    print(a)

def reversing():
    a=[1,2,3,4]
    a.reverse()
    print(a)

def sorting():
    #usig sort --> sort in place
    #sorted -> returns new sorted list without changing original
    a=[1,5,2,9]
    a.sort()
    print(a)

    #reverse sort -> descending
    a.sort(reverse=True)
    print(a)



if __name__ == "__main__":
    create_list()
    print("***************************************")
    deleting()
    print("***************************************")
    appending()
    print("***************************************")
    extending()
    print("***************************************")
    inserting()
    print("***************************************")
    popout()
    print("***************************************")
    removing()
    print("***************************************")
    reversing()
    print("***************************************")
    sorting()
    print("***************************************")