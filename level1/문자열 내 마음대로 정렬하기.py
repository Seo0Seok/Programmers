def solution(strings, n):
    strings.sort()
    check = [i[n] for i in strings]
    check2 = []
    result = []
        
    for i in zip(check, strings):
        check2.append(i)

    for j in sorted(check2):
        result.append(j[1])

    return result

strings = ["sun", "bed", "car"]
n = 1

print(solution(strings, n))