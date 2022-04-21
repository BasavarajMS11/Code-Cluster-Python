#Indexing starts from 0
def indexing(c):
    print(c[1])

#Slcing
def slicing(v):
    start=0
    end=len(v)
    #slice from first till required
    print(v[:3])
    #Slice with step of 2
    print(v[start:end : 2])
    #slice from given position till end
    print(v[2:])
    #slice till given position
    print(v[:2])
    #Last character
    print(v[-1])
    #set of characters from last
    print(v[-5:])
    #set of characters slicing out last
    print(v[:-4])

def adding_or_concatenating():
    #lists
    a=['red', 'green']+['blue']
    print(a)
    #tuples
    b=('read','write')+('execute',)
    print(b)
    #string
    c='great things' + ' take time'
    print(c)

def multiplying():
    #list
    a=[2,4]*4
    print(a)
    #string
    b='bla'*3
    print(b)
    #tuple
    c=(1,3)*4
    print(c)

def check_element_in():
    #list
    a=['red','green','blue']
    print('green' not in a)
    #string
    b='zeal'
    print('z' in b)
    #tuple
    c=('great','things','take','time')
    print('great' in c)

def iterating():
    a=[1,2,3]
    for item in a:
        print(item)

    b=[2,4,6,8]
    for index, item in enumerate(b):
        print(index,item)

def count_nor_items():
    #list
    a=['red','green','blue']
    print(len(a))
    #string
    b='zeal'
    print(len(b))
    #tuple
    c=('great','things','take','time')
    print(len(c))

#min -> minimum item in a sequence lexicographically(alpha or numeric, but cannot mix both types)
def min_lexographically():
    #list
    a=['red','green','blue']
    print(min(a))
    #string
    b='zeal'
    print(min(b))
    #tuple
    c=('the great','things','take','time')
    print(min(c))

def max_lexographically():
    #list
    a=['red','green','blue']
    print(max(a))
    #string
    b='zeal'
    print(max(b))
    #tuple
    c=('the great','things','take','time')
    print(max(c))

def built_in_operations():
    #sum of numeric list
    a=[1,2,3,4,5]
    print(sum(a))
    print(sum(a[:-1]))

    #sum of tuple values
    b=(1,3,5,7)
    print(sum(b))

def sorting():
    #list
    a=['red','green','blue']
    print(sorted(a))
    #string
    b='zeal'
    print(sorted(b))
    #tuple
    c=('the great','things','take','time')
    print(sorted(c))

#Sorting by other letters than first --> Using lambda function
def sorting_by_other_letter():
    c=('the great','things','take','time')
    #sorting by third letter
    print(sorted(c,key=lambda k:k[2]))

def count_items_insequence():
    #list
    a=['red','green','blue','green']
    print(a.count('green'))
    #string
    b='all zeal'
    print(b.count('l'))
    #tuple
    c=('the great','things','take','time')
    print(c.count('time'))

def indexof_items_insequence():
    #list
    a=['red','green','blue','green']
    print(a.index('green'))
    #string
    b='all zeal'
    print(b.index('l'))
    #tuple
    c=('the great','things','take','time')
    print(c.index('time'))

def unpacking_items():
    a=['red','green','blue']
    r,g,b=a
    print(r,g,b)

colors=['red','green','blue']
indexing(colors)
print("...........................")
word='Unbeatable'
slicing(word)
print("...........................")
adding_or_concatenating()
print("...........................")
multiplying()
print("...........................")
check_element_in()
print("...........................")
iterating()
print("...........................")
count_nor_items()
print("...........................")
min_lexographically()
print("...........................")
max_lexographically()
print("...........................")
built_in_operations()
print("...........................")
sorting()
print("...........................")
sorting_by_other_letter()
print("...........................")
count_items_insequence()
print("...........................")
indexof_items_insequence()
print("...........................")
unpacking_items()