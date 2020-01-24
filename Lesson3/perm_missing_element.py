def solution(A):
      A_set = set(A)
  A_set.add(0)
  A_complete = set(range(len(A_set) + 1))
  result = list(A_complete.difference(A_set))
  return result[0]