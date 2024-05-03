def solution(x1, x2, x3, x4):
    answer = True
    a = check_1(x1, x2)
    b = check_1(x3, x4)
    return check_2(a, b)
    
def check_1(x, y):
    if x == False and y == False:
        return False
    else:
        return True

def check_2(x, y):
    if x == True and y == True:
        return True
    else:
        return False