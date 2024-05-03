def solution(absolutes, signs):
    answer = 0
    for x, y in zip(absolutes, signs):
        if y == True:
            x = x
        else:
            x = -x
        answer += x
    return answer