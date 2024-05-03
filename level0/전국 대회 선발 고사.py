def solution(rank, attendance):
    new = []
    for a, b in zip(rank, attendance):
        if b == True:
            new.append(a)
    new.sort()
    return rank.index(new[0]) * 10000 + rank.index(new[1]) * 100 + rank.index(new[2])
       

rank = [3, 7, 2, 5, 4, 6, 1]
attendance = [False, True, True, True, True, False, False]

rank2 = [1, 2, 3]
attendance2 = [True, True, True]

rank3 = [6, 1, 5, 2, 3, 4]
attendance3 = [True, False, True, False, False, True]

print(solution(rank, attendance))
print(solution(rank2, attendance2))
print(solution(rank3, attendance3))