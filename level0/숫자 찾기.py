def solution(num, k):
    answer = 0
    if str(num).find(str(k)) == -1:
        return -1
    return str(num).find(str(k))+1

num = 123
k = 4
print(solution(num, k))