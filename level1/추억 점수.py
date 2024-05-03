def solution(name, yearning, photo):
    answer = []
    for i in photo:
        sum = 0
        for x, y in zip(name, yearning):
            if x in i:
                sum += y
        answer.append(sum)
    return answer