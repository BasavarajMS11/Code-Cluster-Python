'''
Finding all primes upto N in O(N*log(log(N)))
Seive of eratosthenes

1.Basic Approach: O(N*sqrt(N))
for each 1 :N
    traverse and check for every number prime or not

2.Optimized
Remove every number divisible by prime number and greater than sqr(prime)
n=50
2 3 5 7
11 13 17 19
23 29
31 37
41 43 47

'''

from math import *

def generateprimes(n):
    primes=[True]*(n+1)
    primes[0]=False #0 is not prime
    primes[1]=False
    for i in range(2,int(sqrt(n))+1):
        if primes[i] == True:
            for i in range(i*i, n+1,i):
                primes[i]=False
    for i in range(0, len(primes)):
        if primes[i] == True:
            print(i,end=" ")  

T=int(input())
for i in range(T):
    N=int(input())
    generateprimes(N)