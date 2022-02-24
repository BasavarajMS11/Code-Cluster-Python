'''
Bitwise operations
AND : &
OR  : |
NOT : ~
XOR : ^
Right Shift : >>  : Divide in power of 2
Left Shift  : <<  : Multiply in power of 2
'''
#And : To find whether a number is even or odd
def evenorodd(n):
    if n&1 == 1: # Any number and with 1 gives 1 
        print("Odd")
    else:
        print("Even")

def dividepowerof(a,b): #Right shift a by b
    return a >> b

def multiplypowerof(a,b): #Left shift a by b
    return a << b

T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    #N=int(input())
    #evenorodd(N)
    print(dividepowerof(A,B))
    print(multiplypowerof(A,B))