def solution(numbers, k):
    a = []
    for i in range(k):
        a.append(1 + 2*i)
    if a[-1] % len(numbers) == 0:
        return numbers[-1]
    return a[-1] % len(numbers)

numbers = [1,2,3]
k = 5
[1,3,5,7,9]

[1,3,5,7,9,11,13,15,17,19]
print(solution(numbers,k))