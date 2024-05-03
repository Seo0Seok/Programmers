def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
    if len(answer) > k:
        for _ in range(len(answer) - k):
            answer.pop()    
        return answer
    elif len(answer) == k:
        return answer
    else:
        for _ in range(k - len(answer)):
            answer.append(-1)
        return answer

arr = [0,1,1,2,2,3]
k = 3

arr2 = [0,1,1,1,1]
k2 = 4

print(solution(arr, k))
print(solution(arr2, k2))