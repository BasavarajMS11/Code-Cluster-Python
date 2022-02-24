'''
Number of 1's in binary representation of int
3 -> 11  ans =2
6 -> 110 ans =2
'''

def bruteforcecountonesbits(n): #O(N)
    s = str(bin(n))[2:] #since binary value in python--> for 5 is 0b101 slice out first 2--> 101
    print("{}".format(s))
    return s.count('1')

def countonesbits(n): #O(logN)
    onescount=0
    while n:
        onescount+=1
        n=n & (n-1)
    return onescount

T=int(input())
for i in range(T):
    N=int(input())
    print(bruteforcecountonesbits(N))
    print(countonesbits(N))