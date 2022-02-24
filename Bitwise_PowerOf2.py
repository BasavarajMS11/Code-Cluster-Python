'''
Is N power of 2: True or False
Ex: 
N=512 , O/P: TRUE
N=256 , O/P: TRUE
'''

def ispowerof2(n): #O(1)
    if n<=0:
        return False
    a=n
    b=not(n & (n-1)) #Bitwise and
    return a and b

T=int(input())
for i in range(T):
    N=int(input())
    print(ispowerof2(N))