def solution(A, K):
    # write your code in Python 3.6
    if A:
        K %= len(A)
    return A[-K:] + A[:-K]
    return A