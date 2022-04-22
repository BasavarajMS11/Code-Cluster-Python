'''
Queues: FIFO
------------
First In First Out
Enqueue - add an item to end of line/queue
Dequeue - remove an item from front of line/queue

Usecases:
--------
Q's anything you wait
Bank tellers, Placing orders, Supermarket checkout etc
'''

'''
Queue using Python Deque (Double ended queue built in)
Use append() to enqueue an item
Use popleft() to dequeue an item
'''
from collections import deque

#1. Using built in deque library to implement single ended queue
def queue_using_deque():
    myqueue= deque()
    myqueue.append(2)
    myqueue.append(4)
    myqueue.append(3)
    print(myqueue)
    print(myqueue.popleft())
    print(myqueue)
    print(myqueue.popleft())
    print(myqueue)

#1. Using built in deque library with wrapper class to implement single ended queue
class Queue():

    def __init__(self) -> None:
        self.queue=deque()

    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue)>0:
            return self.queue.popleft()
        else:
            return None
    
    def __str__(self) -> str:
        return str(self.queue)


if __name__=="__main__":

    #1. Using built in deque library to implement single ended queue
    queue_using_deque()

    #2. Using built in deque library with wrapper class to implement single ended queue
    myqueue= Queue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(5)
    myqueue.enqueue(3)
    print(myqueue)
    print(myqueue.dequeue())
    print(myqueue)
    print(myqueue.dequeue())
    print(myqueue)