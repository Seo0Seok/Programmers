# def solution(n):
#     if n % n ** (1/2) == 0:
#         answer = 1
#     else:
#         answer = 2
#     return answer


def solution(n):
    
    return 1 if n % n ** (1/2) == 0 else 2

n = 976
print(solution(n))