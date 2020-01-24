def solution(X, Y, D):
    # write your code in Python 3.6
  if(X==Y):
    return 0
  elif((X-Y) % D == 0):
    return (Y-X)//D
  else:
    return (Y-X)//D + 1