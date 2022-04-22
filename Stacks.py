'''
Stacks: LIFO
Push - push item to stack at top
Pop - pop out item from stack from top
Peek - get item on top of stack without removing
Clear - clears all item from stack

Usecase - Command stack maintaining order of execution and "undo"
'''

'''
Stack using list
----------------
Use append() to push item onto stack
Use pop() to remove an item
'''
#1.Stack using list
def stack_using_list():
    #Define list as to store stack elements
    mystack= list()

    #Push elements to stack using append
    mystack.append(2)
    mystack.append(4)
    mystack.append(6)
    mystack.append(3)
    print(mystack)

    #Pop elements using pop
    print(mystack.pop())
    print(mystack.pop())
    print(mystack)

#2. Stack using list with wrapper class - for additional functionalities
class Stack():
    def __init__(self) -> None:
        self.stack=list()

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else:
            return None
            
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None

    def __str__(self) -> str:
        return str(self.stack)

if __name__=="__main__":
    #1. Stack using list
    stack_using_list()

    #2.Stack using list with wrapper class
    mystack=Stack()
    mystack.push(10)
    mystack.push(20)
    print(mystack)
    print(mystack.pop())
    print(mystack.peek())
    print(mystack.pop())
    print(mystack.pop())

