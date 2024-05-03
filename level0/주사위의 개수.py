def solution(box, n):
    (a, b, c) = box
    return (a // n) * (b // n) * (c // n)

box = [10,8,6]
n = 3
print(solution(box, n))