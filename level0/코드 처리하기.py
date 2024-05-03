def solution(code):
    mode = 0
    ret = ''

    for idx, i in enumerate(code):
        if mode == 0:
            if i != "1" and idx % 2 == 0:
                ret += i
            elif i == "1":
                mode = 1
        elif mode == 1:
            if i != "1" and idx % 2 == 1:
                ret += i
            elif i == "1":
                mode = 0
    if ret == '':
        ret = "EMPTY"
    return ret

code = "abc1abc1abc"
print(solution(code))