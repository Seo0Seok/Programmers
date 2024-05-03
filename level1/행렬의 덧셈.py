def solution(arr1, arr2):
    answer = []
    answer2 = []

    for x, y in zip(arr1, arr2):
        for j in range(len(arr2[0])):
            answer.append(x[j] + y[j])
        answer2.append(answer)
        answer = []

    return answer2

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

# arr1 = [[1],[2]]
# arr2 = [[3],[4]]

print(solution(arr1, arr2))