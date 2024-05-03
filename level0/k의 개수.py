def solution(i, j, k):
    answer = 0
    for i in range(i, j+1):
        if str(i).count(str(k)) == 1:
            answer += 1
        else:
            answer += str(i).count(str(k))
    return answer

i = 3
j = 10
k = 2
print(solution(i, j, k))