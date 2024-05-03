def solution(n):
    answer = []
    i, j = 0, 0
    x, y = 0, 1

    for _ in range(n):
        answer.append([0] * n)
    
    for k in range(1, n*n+1):
        answer[i][j] = k
        ni, nj = i + x, j + y

        if 0 <= ni < n and 0 <= nj < n and answer[ni][nj] == 0:
            i, j = ni, nj
        else:
            x, y = y, -x
            i, j = i + x, j + y
            
    return answer

n = 4
print(solution(n)) 