'''
Let element accessing at index "i"
then,
parent(i) = i/2
leftchild(i) = i*2
rightchild(i) = (i*2)+1
-------------------------
Float Up-> Smallest 
Bubble Down -> Smallest to delete
---------------------------------

Operations of MinHeaps
-Push - Insert ( Add value at end then float it up to it's proper position)
-Peek - get min ( Return value at heap[1])
-Pop - remove min (Move min to end , Delete it, Bubble down item at index 1 to it's position, return min)

MinHeap - bubbles lowest value at the top
Public Functions: push, peek, pop
Private Functions: swap, __floatUp, __bubbleDown, __str
'''

class MinHeap:
    def __init__(self, items=[]) -> None:
        super().__init__()
        self.heap = [0] #Index starts from 1
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap)-1)

    def push(self,data):
        self.heap.append(data)
        self.__floatUp(len(self.heap)-1)

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def  pop(self):
        if len(self.heap)>2:
            self.__swap(1, len(self.heap)-1)
            min=self.heap.pop()
            self.__bubbleDown(1)
        elif len(self.heap) == 2:
            min=self.heap.pop()
        else:
            min=False
        return min

    def __swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __floatUp(self, index):
        parent=index//2
        if index <=1:
            return
        elif self.heap[index]<self.heap[parent]:
            self.__swap(index,parent)
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left=index*2
        right=index*2 + 1
        smallest = index
        if len(self.heap) > left and self.heap[smallest] > self.heap[left]:
            smallest =left
        if len(self.heap) > right and self.heap[smallest ] > self.heap[right]:
            smallest =right
        if smallest  != index:
            self.__swap(index, smallest )
            self.__bubbleDown(smallest )

    def __str__(self) -> str:
        return str(self.heap)

if __name__=="__main__":
    mh= MinHeap([9,15,20])
    print(mh)
    mh.push(10)
    print(mh)
    print(mh.pop())
    print(mh)
    print(mh.peek())