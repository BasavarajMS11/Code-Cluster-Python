'''
Convert N to it's binary representation and visa versa
'''
def intToBin(n):
    return str(bin(n))[2:]

def binToInt(s):
    return int(s,2)

T=int(input())
for i in range(T):
    N=int(input())
    binstr=intToBin(N)
    integer=binToInt(binstr)
    print(N, binstr,integer,N==integer)