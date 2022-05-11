'''
Indirect Recursion: Two functions calling each other 
'''

def fun_1(n):
    if n>0:
        print(n)
        fun_2(n-1)

def fun_2(n):
    if n>0:
        print(n)
        fun_1(n-1)

if __name__=="__main__":
    n=3
    fun_1(n)