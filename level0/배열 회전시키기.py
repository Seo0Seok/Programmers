def solution(numbers, direction):
    if direction == 'right':
        numbers = [numbers[-1]] + numbers[:-1]
    else:
        numbers = numbers[1:] + [numbers[0]]
    return numbers

numbers = [1,2,3]
direction = 'left'

print(solution(numbers, direction))