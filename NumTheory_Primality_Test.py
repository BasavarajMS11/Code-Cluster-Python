'''
Prime Number: 2 factors 1 and itself
'''
from math import *


def prime1(n): #O(N)
    divisorcount=0
    for i in range(1, n+1):
        if n%i==0:
            divisorcount+=1
    #print(divisorcount)
    if divisorcount==2:
        return True
    else:
        return False

def prime2(n): #O(sqrt(N))
    if n==0 or n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2 == 0 or n%3== 0:
        return False
    for i in range(5, int(sqrt(n))+1):
        if n%i==0 or n%(i+2)==0:
            return False
    return True



T=int(input())
for i in range(T):
    N=int(input())
    print(prime1(N))
    #print(prime2(N))