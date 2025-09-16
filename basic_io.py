"""
File: basic_io.py
Description:
Basic Input/Output operations in Python
This module contains functions to demonstrate basic input/output operations in python.
Each function reads input in a specific format and prints the output accordingly.
It is useful for competitive programming and basic data handling tasks.
"""

"""
Integer: Read an integer from the input and print it.
"""


def read_int():
    i = int(input())
    print(i)


"""
String: Read a string from the input and print it.
"""


def read_string():
    s = input()
    print(s)


# Multiple values - 1.Using Map
"""
Read multiple integers from the input using map and ptint them.
"""


def read_multimap():
    a, b, c = map(int, input().split())
    print(a, b, c)


# Multiple values - 2.Using list
def read_multilist():
    values = [int(i) for i in input().split()]
    print(values)
    print(sum(values))


# Number of elements followed by elements
"""
Format:
5
1 0 1 0 1
"""


def read_numelements():
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(arr)


"""Format:
3
1
2
3"""


def read_numelements_2():
    n = int(input())
    for i in range(n):
        value = int(input())


# Read test case followed by arrays
"""Format
2
4
1 2 3 4
3
1 2 3"""


def read_testcase_arrays():
    t = int(input())  # number of test cases
    for i in range(t):
        n = int(input())
        arr = [int(i) for i in input().split()]
    print("success")


# Matrix of n x n given n
"""
4
1 2 3 4
1 4 5 8
2 4 8 6
2 7 9 0
"""


def read_matrix():
    n = int(input())
    for i in range(n):
        mat = [int(i) for i in input().split()]
    print(mat)


# Output elements of array - in new line
"""
arr=[1,2,3]
O/P:
1
2
3
"""


def out_array_newline():
    arr = [1, 2, 3]
    for i in arr:
        print(i)


def out_array_newline2():
    arr = [1, 2, 3]
    for i in range(0, 3):
        print(arr[i])


# Output elements of array - in single line
"""
arr=[1,2,3]
O/P:
1
2
3
"""


def out_array_singleline():
    arr = [1, 2, 3]
    for i in arr:
        print(i, end=" ")


# Output - Integer range of values
def out_int_range():
    for i in range(1, 10):
        print(i)


def out_int_range2():
    for i in range(0, 10, 2):  # range of values with difference of 2
        print(i)


# main function
if __name__ == "__main__":
    # read_int()
    # read_string()
    # read_multimap()
    # read_multilist()
    # read_numelements()
    # read_numelements_2()
    # read_testcase_arrays()
    # read_matrix()
    # out_array_newline()
    # out_array_newline2()
    # out_array_singleline()
    # out_int_range()
    out_int_range2()
