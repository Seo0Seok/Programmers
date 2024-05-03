def solution(emergency):
    answer = []
    sort_emergency = sorted(emergency,reverse=True)
    for i in emergency:
        for j in sort_emergency:
            if i == j:
                answer.append(sort_emergency.index(j) + 1)
    return answer

emergency = [30, 10, 23, 6, 100]

print(solution(emergency))