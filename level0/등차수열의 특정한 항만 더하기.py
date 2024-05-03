def solution(a, d, included):
    answer = 0
    for idx, i in enumerate(included):
        if i == True:
            answer += (a + (idx * d))
    return answer

a = 7
d = 1
included = [False, False, False, True, False, False, False]
print(solution(a, d, included))