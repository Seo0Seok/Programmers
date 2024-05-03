def solution(spell, dic):
    listt = []
    for i in dic:
        answer = 0
        for j in spell:
            if j in i:
                answer += 1
        if answer == len(spell):
            return 1
    return 2
    
spell = ["s", "o", "m", "d"]
dic = ["moos", "dzx", "smm", "sunmmo", "som"]

print(solution(spell, dic))