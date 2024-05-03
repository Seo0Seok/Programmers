def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)

    for i in range(2, max(denom, numer)):
        while denom % i == 0 and numer % i == 0:
            denom //= i
            numer //= i
    return [numer, denom]

numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

print(solution(numer1, denom1, numer2, denom2))