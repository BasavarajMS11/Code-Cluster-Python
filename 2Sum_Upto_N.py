#Sum upto N
'''
n=3 => sum= 1+2+3 = 6
'''
def sum(n): #O(1) --> Efficient
    return (n)*(n+1)//2

def sum2(n): #O(N)
    value=0
    for i in range(1,n+1):
        value+=i
    return value

T=int(input())
for i in range(T):
    N=int(input())
    print("Sum:{}".format(sum(N)))
    print("Sum2:{}".format(sum2(N)))