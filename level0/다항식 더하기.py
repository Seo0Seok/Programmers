def solution(polynomial):
    answer = ''
    x_num = 0
    num = 0

    polynomial = polynomial.split(' + ')
    for i in polynomial:
        if 'x' not in i:
            num += int(i)
        else:
            if i == 'x':
                x_num += int(i.replace('x', '1'))
            else:
                x_num += int(i.replace('x',''))

    if x_num != 0 and num != 0:
        if x_num == 1:
            x_num = ""
        return str(x_num) + "x" + " + " + str(num)
    elif num == 0:
        if x_num == 1:
            x_num = ""
        return str(x_num) + "x"
    elif x_num == 0:
        return str(num)
    
    

polynomial = "x + 1"

print(solution(polynomial))