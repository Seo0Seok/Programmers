def solution(a, b):
    # 기약분수 만들기
    for i in range(2, (max(a,b)+1)):
        while a % i == 0 and b % i == 0:
            a //= i
            b //= i
    
    # 처음부터 기약분수면 분모 소인수 확인
    for j in range(2, b+1):
        while b % j == 0:
            b //= j
            if j not in [2, 5]:
                return 2
    return 1
    

a = 31
b = 14
print(solution(a,b))