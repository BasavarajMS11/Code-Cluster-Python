#Euclid Algorithm : O(log(min(a,b)))
#Product(a,b)= LCM(a, b) * GCD (a, b)
def GCD(a,b):
    if a==0:
        return b
    return GCD(b%a,a)

def LCM(a,b):
    prod = a*b
    hcf = GCD(a,b)
    return prod//hcf

T= int(input())
for i in range(T):
    A,B=map(int,input().split())
    #X=GCD(A,B)
    #print(X)
    print("GCD {} , LCM {}  ".format(GCD(A,B),LCM(A,B)))
