def solution(n, t):
    a = n * 2
    if t > 1:
        a *= 2 ** (t-1)
    return a 

def solution(n, t):
    return n << t


print(solution(7,15))


