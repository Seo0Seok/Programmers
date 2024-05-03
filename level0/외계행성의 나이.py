def solution(age):
    answer = ''
    alpha = list("abcdefghijklmnopqrstuvwxyz") 

    for i in str(age):
        answer += alpha[int(i)]
    return answer

age = 100
print(solution(age))
