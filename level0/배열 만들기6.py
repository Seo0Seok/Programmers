def solution(arr):
    stk = []
    i = 0

    while(i < len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] == arr[i]:
                stk.pop()
                i += 1
            else:
                stk.append(arr[i])
                i += 1
    if len(stk) == 0:
        return [-1]
    return stk

arr = [0, 1, 1,0]
# arr = [0, 1, 0, 1, 0]
# arr = [0, 1, 1, 0]
print(solution(arr))
