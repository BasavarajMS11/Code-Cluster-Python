'''
In an array [1, 2, 3, 2, 1]
3 is occuring only once --> Return 3
To find number occuring only once
Using XOR operation: N ^ N = 0
                     N ^ 0 = N
'''
def findsingleoccurringelement(arr):
    res = arr[0]
    for i in range(1,len(arr)):
        res = res ^ arr[i]
    return res

T= int(input())
for i in range(T):
    array = list(map(int, input().split()))
    print(findsingleoccurringelement(array))
