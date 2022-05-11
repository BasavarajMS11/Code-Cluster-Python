'''
Recursion: 
- Function calling itself directly or indirectly
- Use Cases:Factorial, Power, Series - Fibonacci, TOH, Traversals - Tree, Graph
- Recurion has 2 phases - Calling phase and Returning phase
- Stack is used in recursion
- Recurrence relation - Time complexity
- Types of recursions: Head, Tail, Indirect, Tree, Nested

'''
def fun(x):
    if x==0:
        return 0
    else:
        print(x)
        return fun(x-1)+x

if __name__=="__main__":
    n=10
    print(fun(n))