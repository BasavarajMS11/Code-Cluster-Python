'''
Head Recursion:
Function call at first and rest operations such as print,add are next
'''
def head_rec(n):
    if n==0:
        return
    else:
        head_rec(n-1) 
        print(n)   

if __name__ == "__main__":
    n=5
    head_rec(5)
