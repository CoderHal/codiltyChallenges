def solution(N, A):

    A_len = len(A)
    counters = [0] * N
    max_result = 0
    max_counter = 0

    for i in range(A_len):
        if A[i] == N + 1:
            max_result = max(max_result, max_counter)
        else:
            if counters[A[i] - 1] < max_result:
                counters[A[i] - 1] = max_result

            counters[A[i] - 1] += 1
            max_counter = max(max_counter, counters[A[i] - 1])

    for i in range(N):
        counters[i] = max(max_result, counters[i])

    return counters