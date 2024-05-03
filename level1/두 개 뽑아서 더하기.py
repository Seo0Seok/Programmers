from itertools import combinations
def solution(numbers):
    answer = []
    answer.append(list(set(sum(i) for i in list(combinations(numbers, 2)))))
    return sorted(answer[0])

numbers = [5,0,2,7]
print(solution(numbers))