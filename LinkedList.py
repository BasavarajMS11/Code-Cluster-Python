'''
Every node has 2 parts- Data and Next(Ptr to next node)
Start node -> root node

Attributes
------------
root - pointer to the beginning of list
size - number of nodes in list

Operations
----------
add(data)
remove(data)
find(data)
print_list()
-------------

Node class
-has constructor and sets data
-has members next_node and prev_node(for doubly)

Linked List Class:
Has 2 attributes - root
Methods - Add, Remove, Find, Print
'''


class Node:
    def __init__(self,d,n=None,p=None) -> None:
        self.data=d
        self.next_node=n
        self.prev_node=p

    def __str__(self):
        return ('('+str(self.data)+')')

class LinkedList:

    def __init__(self, r=None) -> None:
        self.root=r
        self.size=0

    def add(self,d):
        new_node = Node(d, self.root)
        self.root= new_node
        self.size+=1

    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.data==d:
                return 
            else:
                this_node=this_node.next_node
        return None

    def remove(self,d):
        this_node=self.root
        prev_node=None

        while this_node is not None:
            if this_node.data == d:
                if prev_node is not None: #Data is in non root
                    prev_node.next_node=this_node.next_node
                else: #Data is in root node
                    self.root = this_node.next_node
                self.size-=1
                return True
            else:
                prev_node=this_node
                this_node=this_node.next_node
        return False

    def print_list(self):
        this_node=self.root
        while this_node is not None:
            print(this_node, end='->')
            this_node=this_node.next_node
        print('None')

if __name__=="__main__":
    myList= LinkedList()
    myList.add(2)
    myList.add(5)
    myList.add(6)
    myList.print_list()

    print("Size: "+str(myList.size))
    myList.remove(6)
    print("Size: "+str(myList.size))
    print(myList.find(2))
    print(myList.root)




