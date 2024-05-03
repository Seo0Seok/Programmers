def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

# 최대공약수
def gcd(n, m):
    check = []
    for i in range(2, max(n, m) + 1):
        if max(n, m) % i == 0 and min(n, m) % i == 0:
            check.append(i)
    return max(check) if len(check) > 0 else 1
            
# 최소공배수
def lcm(n, m):
    check = []
    if gcd(n, m) == 1:
        return n * m
    else:
        for i in range(2, n * m):
            if i % n == 0 and i % m == 0:
                check.append(i)
        if len(check) > 0:
            return min(check) 
        
    
n = 6
m = 4
print(solution(n, m))