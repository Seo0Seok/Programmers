def solution(k, score):
    answer = []
    result = []
    cnt = 1
    for i in range(1, len(score)+1):
        if i <= k:
            answer.append(score[i-1])
            result.append(min(answer))
        elif i > k:
            answer.append(score[i-1])
            result.append(min(sorted(answer)[cnt:]))
            cnt += 1
    return result

k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k, score))