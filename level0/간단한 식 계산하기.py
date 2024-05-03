def solution(binomial):
    answer = 0
    if '+' in binomial:
        binomial = binomial.split('+')
        answer = int(binomial[0]) + int(binomial[1])

    elif '-' in binomial:
        binomial = binomial.split('-')
        answer = int(binomial[0]) - int(binomial[1])

    else:
        binomial = binomial.split('*')
        answer = int(binomial[0]) * int(binomial[1])

    return answer
