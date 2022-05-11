'''
Tail Recursion:
Function call at last and rest operations such as print are before
'''
def tail_rec(n):
    if n==0:
        return 0
    else:
        print(n)
        return tail_rec(n-1)     

if __name__ == "__main__":
    n=5
    tail_rec(5)
