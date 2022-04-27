'''
Circular Linked List: 
End node points to root node
Usecase: Modeling continuous looping objects(Monopoly or race track)
'''

class Node:
    def __init__(self,d,n=None,p=None) -> None:
        self.data=d
        self.next_node=n 
        self.prev_node=p

    def __str__(self) -> str:
        return ('('+str(self.data)+')')

class CircularLinkedList:
    def __init__(self, r=None) -> None:
        self.root=r
        self.size=0

    def add(self, d):
        if self.size==0:
            self.root=Node(d)
            self.root.next_node = self.root
        else:
            new_node= Node(d,self.root)
            this_node=self.root
            while this_node.next_node!=self.root:
                this_node=this_node.next_node
            this_node.next_node=new_node
            self.root=new_node
        self.size+=1

    def find(self, d):
        this_node=self.root
        while True:
            if this_node.data==d:
                return d
            elif this_node.next_node == self.root:
                return False
            this_node=this_node.next_node

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while True:
            #If found
            if this_node.data==d:
                #If root
                if prev_node is None:
                    #Traverse till end
                    while this_node.next_node != self.root:
                        this_node=this_node.next_node
                    this_node.next_node = self.root.next_node
                    self.root= self.root.next_node
                else:
                   prev_node.next_node=this_node.next_node
                self.size-=1
                return True
            #Not found
            elif this_node.next_node == self.root:
                return False
            prev_node=this_node
            this_node=this_node.next_node

    def print_list(self):
        if self.root is None:
            return
        this_node=self.root
        print(this_node, end='->')
        while this_node.next_node != self.root:
            this_node=this_node.next_node
            print(this_node,end='->')

if __name__ == "__main__":
    cll=CircularLinkedList()

    cll.add(5)
    cll.add(3)
    cll.add(8)
    cll.add(7)
    cll.add(1)
    cll.print_list()

    print("\nSize of Circular LL: "+str(cll.size))
    print(cll.find(2))
    print(cll.find(3))

    cll.remove(8)
    cll.print_list()

    