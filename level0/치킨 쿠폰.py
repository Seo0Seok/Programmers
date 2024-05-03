def solution(chicken):
    coupon = 0
    service = 0

    while True:
        coupon += chicken % 10
        chicken //= 10
        service += chicken

        if coupon >= 10:
            coupon -= 10
            service += 1
            chicken += 1
        if chicken == 0:
            break
      
    return service


chicken = 1999
print(solution(chicken))