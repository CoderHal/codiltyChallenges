# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6

    difference = B - A
    remainder = A % K
    if A % K == 0:
        res = ((difference // K)+1)
    else:
        res = (difference + remainder) // K
    return res


    