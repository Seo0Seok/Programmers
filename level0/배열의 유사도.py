def solution(s1, s2):
    answer = 0   
    for i in range(len(s2)):
        answer += s1.count(s2[i])
    return answer


s1 = ["n", "omg"]
s2 = ["m", "dot"]

print(solution(s1, s2))
