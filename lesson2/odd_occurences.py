from collections import Counter

def solution(A):
  frq = Counter(A)
  for key in frq:
    if frq[key] % 2 == 1:
      return key