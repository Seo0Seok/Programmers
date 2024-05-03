def solution(intStrs, k, s, l):
    answer = []
    for a in intStrs:
        if int(a[s:s+l]) > k:
            answer.append(int(a[s:s+l]))
    return answer

intStrs = ["0123456789","9876543210","9999999999999"]
k = 50000
s = 5
l = 5

print(solution(intStrs, k, s, l))