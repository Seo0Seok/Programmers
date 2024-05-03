def solution(ineq, eq, n, m):
    answer = 0
    a = ineq + eq
    if ineq == "<" and eq == "=":
        answer = n <= m
    elif ineq == "<" and eq == "!":
        answer = n < m
    elif ineq == ">" and eq == "=":
        answer = n >= m
    else:
        answer = n > m
    return int(answer)
    

ineq = ">" 
eq = "!"
n = 41
m = 78

print(solution(ineq,eq, n, m))