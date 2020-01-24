def solution(A):
    # write your code in Python 3.6
    expected = set(range(1, len(A)+1))
    given = set(A)
    return int(expected == given)