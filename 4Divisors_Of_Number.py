
'''
Example:
N=12
[1,2,3,4,6,12]
'''
from math import *

def Divisors(n): #O(N)
    divisors=[]
    for i in range(1,n+1):
        if n%i==0:
            divisors.append(i)
    return divisors

def Divisors2(n): #O(sqrt(N)) --> Efficient
    divisors=set()
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            divisors.add(i)
            divisors.add(n//i)
    return divisors


T=int(input())
for i in range(T):
    N=int(input())
    ans=Divisors(N)
    print(*ans)
    ans2=Divisors2(N)
    print(*ans2)