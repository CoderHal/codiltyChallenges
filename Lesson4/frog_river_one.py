def solution(X, A):
    # write your code in Python 3
    if len(set(A)) < X: 
        return -1
    path = set(A[:X])
    for time in range(X-1, len(A)):
        path.add(A[time])
        if len(path) == X:
            return time