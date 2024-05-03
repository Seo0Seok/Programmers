def solution(a, b):
    return str(eval(a + "+" + b))


def solution2(a, b):
    answer = int(a) + int(b)
    return str(answer)

a = "582"
b = "734"

print(solution(a,b))
print(solution2(a,b))