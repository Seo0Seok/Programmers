def solution(arr, flag):
    answer = []
    for i in range(len(flag)):
        if flag[i] == True:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            for _ in range(arr[i]):
                answer.pop()
    return answer

arr = [3, 2, 4, 1, 3]
flag = [True, False, True, False, False]

print(solution(arr,flag))