def solution(d, budget):
    answer = 0
    d.sort()
    for idx, i in enumerate(d):
        budget -= i
        if budget == 0 or ((budget > 0) and len(d) == 1):
            return idx + 1
        elif budget < 0:
            return idx
    return len(d)
d = [1,1,1,1,1]
budget = 10

print(solution(d, budget))

    