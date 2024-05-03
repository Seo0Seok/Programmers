def solution(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == arr[j][i]:
                cnt += 1
    if cnt == (len(arr)*len(arr)):
        return 1
    else:
        return 0
    