from itertools import combinations

def solution(number):
    answer = 0
    combi_list = list(combinations(number, 3))
    for i in combi_list:
        if sum(i) == 0:
            answer += 1
    return answer


number = [-3, -2, -1, 0, 1, 2, 3]
print(solution(number))