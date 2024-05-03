# def solution(strlist):
#     answer = []
#     for i in strlist:
        
#         answer.append(len(i))
#     return answer


def solution(strlist):
    answer = list(map(len, strlist))
    return answer


strlist = ["We", "are", "the", "world!"]

print(solution(strlist))