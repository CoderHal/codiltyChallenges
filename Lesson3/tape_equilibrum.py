def solution(A):
    # write your code in Python 3.6
    sum1 = A[0]
    sum2 = sum(A[1:])
    diff = abs(sum1 - sum2)
    for i in range(1, len(A) - 1):
        sum1 += A[i]
        sum2 -= A[i]
        if abs(sum1 - sum2) < diff:
            diff = abs(sum1 - sum2)
    return diff