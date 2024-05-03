def solution(numlist, n):
    answer =[] 
    result = []

    for i in numlist:
        answer.append(i-n)

    for j in sorted(answer, key=lambda x:(abs(x), -x)):
        result.append(numlist[answer.index(j)])

    return result

numlist = [10000,20,36,47,40,6,10,7000]
n = 30
# 정답 = [36, 40, 20, 47, 10, 6, 7000, 10000]
print(solution(numlist, n))