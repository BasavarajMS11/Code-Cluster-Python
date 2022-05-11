'''
Tree Recursion - Function calling itself for more than once
'''
def tree_rec(n):
    if n>0:
        tree_rec(n-1)
        print(n)
        tree_rec(n-1)

if __name__=="__main__":
    n=3
    tree_rec(n)