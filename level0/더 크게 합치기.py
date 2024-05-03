def solution(a, b):
    answer = int(str(b) + str(a))
    if int(str(a) + str(b)) >= int(str(b) + str(a)):
        answer = int(str(a) + str(b))
    return answer