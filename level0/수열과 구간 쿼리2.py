def solution(arr, queries):

    result = []

    for s, e, k in queries:
        answer = []
        for i in arr[s:e+1]:
            if i > k:
                answer.append(i)
        result.append(answer)  

    for i in range(len(result)):
        if len(result[i]) > 1:
            result[i] = min(result[i])
        elif len(result[i]) == 1:
            result[i] = result[i][0]
        else:
            result[i] = -1

    return result

arr = [0, 1, 2, 4, 3]
queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]

print(solution(arr, queries))
