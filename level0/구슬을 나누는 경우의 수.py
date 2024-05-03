def solution(balls, share):
    answer = factorial(balls) // (factorial(balls-share) * factorial(share))
    return answer

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

balls = 5
share = 3
# print(solution(balls, share))

import math
# help(math.comb)
print(math.comb?)
def solution(balls, share):
    return math.comb(balls, share)
# print(solution(balls, share))