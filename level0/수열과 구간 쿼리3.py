def solution(arr, queries):
    answer = []
    tmp = 0
    for i in queries:
        tmp = arr[i[0]]
        arr[i[0]] = arr[i[1]]
        arr[i[1]] = tmp
    return arr

arr = [0,1,2,3,4]
queries = [[0,3], [1,2], [1,4]]

print(solution(arr, queries))