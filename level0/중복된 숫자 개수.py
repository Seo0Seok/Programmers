def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1

    return answer

array = [0,2,3,4]
print(solution(array, 1))