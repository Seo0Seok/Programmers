def solution(M, N):    
    return (min(M, N) - 1) + ((max(M, N) - 1) * (min(M, N)))

M = 3
N = 3
print(solution(M, N))