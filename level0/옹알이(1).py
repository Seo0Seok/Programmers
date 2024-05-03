def solution(babbling):
    answer = 0
    a = "aya"
    b = "ye"
    c = "woo"
    d = "ma"
    
    for i in babbling:
        if len(i.replace(a, ' ').replace(b, ' ').replace(c, ' ').replace(d, ' ').strip()) == 0:
            answer += 1
    return answer

babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa", "yemaye"]
print(solution(babbling))