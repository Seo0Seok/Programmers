def solution(bin1, bin2):
    a = 0
    b = 0
    c1 = len(bin1) - 1
    c2 = len(bin2) - 1

    for i in bin1:
        a += int(i) * (2 ** c1)
        c1 -= 1

    for j in bin2:
        b += int(j) * (2 ** c2)
        c2 -= 1

    return str(bin(a+b)[2:])

bin1 = "1001"
bin2 = "1111"
# 9, 17
print(solution(bin1, bin2))