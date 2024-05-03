def solution(sides):
    answer = 0
    z = 0
    sides.sort()
    x, y = sides

    while z < x + y:
        z += 1    
        if z <= y and x + z > y:
            answer += 1
        elif z > y and x + y > z:
            answer += 1
    return answer

sides= [11,7]
print(solution(sides))
