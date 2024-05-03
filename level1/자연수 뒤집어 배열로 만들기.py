def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]

n = 12345
print(solution(n))