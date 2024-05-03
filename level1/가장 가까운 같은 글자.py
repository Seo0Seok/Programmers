def solution(s):
    answer = []
    result = []
    
    for i in s:
        if i not in answer:
            answer.append(i)
            result.append(-1)          
        else:
            result.append(answer[::-1].index(i) + 1)
            answer.append(i)

    return result

s = "bananana"
print(solution(s))