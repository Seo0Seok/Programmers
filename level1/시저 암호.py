def solution(s, n):
    answer = ''
    upper_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    
    for i in s:
        if i.isalpha() and i in upper_alpha:
            i = upper_alpha[upper_alpha.index(i)+n]
            answer += i
        elif i.isalpha() and i in lower_alpha:
            i = lower_alpha[lower_alpha.index(i)+n]
            answer += i
        else:
            answer += i
    
    return answer

s = "a B z"
n = 4

print(solution(s, n))

