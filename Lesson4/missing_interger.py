def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    A_min = 1
    for elem in A:
        if elem == A_min:
            A_min+=1
    return A_min