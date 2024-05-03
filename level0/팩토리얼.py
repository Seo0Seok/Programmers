def solution(n):
    j = 1
    for i in range(1, 11):
        j *= i
        if j * (i+1) > n:
            return i
        
n = 3628800

print(solution(n))