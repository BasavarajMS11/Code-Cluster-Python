'''
Doubly Linked List
------------------
Every node has 3 parts: data, pointer to previous node, pointer to next node
- Iterate list in either direction
'''

class Node:
    def __init__(self,d,n=None,p=None) -> None:
        self.data=d
        self.next_node=n 
        self.prev_node=p

    def __str__(self) -> str:
        return ('('+str(self.data)+')')

class DoublyLinkedList:
    def __init__(self, r=None) -> None:
        self.root=r
        self.last=r
        self.size=0
    
    def add(self,d):
        if self.size==0:
            self.root=Node(d)
            self.last=self.root
        else:
            new_node=Node(d,self.root)
            self.root.prev_node=new_node
            self.root=new_node
        self.size+=1
    
    def find(self,d):
        this_node=self.root
        while this_node is not None:
            if this_node.data ==d:
                return d
            elif this_node.next_node == None:
                return False
            else:
                this_node = this_node.next_node
    
    def remove(self,d):
        this_node = self.root
        while this_node is not None:
            if this_node.data == d:
                #Delete root node
                if this_node.prev_node is None:
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                else:
                    #Delete middle node
                    if this_node.next_node is not None:
                        this_node.prev_node.next_node =this_node.next_node
                        this_node.next_node.prev_node =this_node.prev_node
                    #Delete Last Node
                    else:
                        this_node.prev_node.next_node=None
                        self.last=this_node.prev_node
                self.size-=1
                return True
            else:
                this_node = this_node.next_node

        return False

    def print_list(self):
        if self.root is None:
            return
        this_node=self.root
        print(this_node,end="->")
        while this_node.next_node is not None:
            this_node=this_node.next_node
            print(this_node,end="->")
        print()

if __name__ == "__main__":
    dll=DoublyLinkedList()
    dll.add(8)
    dll.add(4)
    dll.add(3)
    dll.add(6)
    dll.add(9)

    dll.print_list()

    print("Size of Doubly LL:"+str(dll.size))
    
    dll.remove(3)
    dll.print_list()
    dll.remove(9)
    dll.print_list()
    dll.remove(8)
    dll.print_list()

    print(dll.find(6))
    print(dll.find(5))
    dll.add(5)
    dll.print_list()






    