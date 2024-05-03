def solution(numbers):
    answer = 0
    for i in "1234567890":
        if int(i) not in numbers:
            answer += int(i)
    return answer