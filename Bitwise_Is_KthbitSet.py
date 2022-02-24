'''
Check of the K th bit is set from right
'''
# K th bit from right
def kthbit(n,k):
    if n & (1 << (k-1)):
        print("set")
    else:
        print("not set")

T= int(input())
for i in range(T):
    N,K=map(int,input().split())
    kthbit(N,K)