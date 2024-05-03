def solution(arr, queries):
    
    for i in range(len(arr)):
        answer = []
        for (s,e) in queries:
            if s <= i and i <= e:
                answer.append(i)
        for k in answer:
            arr[k] += 1
    return arr

arr = [0,1,2,3,4]
queries = [[0, 1],[1, 2],[2, 3]]

print(solution(arr, queries))