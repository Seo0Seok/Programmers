def solution(s):
    answer = []
    for i in s.split():
        if i != "Z":
            answer.append(int(i))
        else:
            answer.pop()
    return sum(answer)
s = "10 Z 20 Z 1"
print(solution(s))