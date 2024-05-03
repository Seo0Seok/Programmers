def solution(n):
    answer = []
    for i in range(n):
        answer.append([0] * n)
        answer[i][i] = 1
    return answer

n = 3
print(solution(n))