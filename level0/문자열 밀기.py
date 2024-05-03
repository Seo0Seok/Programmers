def solution(A, B):
    answer = 0
    check = []
    for i in range(len(A)):
        if B == A[len(A)-i:] + A[:len(A)-i]:
            check.append(i)
    if len(check) == 0:
        return -1
    else:
        return min(check)

A = "abc"
B = "abc"

print(solution(A, B))