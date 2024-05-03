def solution(myString):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    answer = ''
    for i in myString:
        if i in alpha:
            i = 'l'
        answer += i
    return answer

myString = "abcdevwxyz"

print(solution(myString))


