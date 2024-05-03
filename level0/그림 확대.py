def solution(picture, k):
    answer = [""] * len(picture)
    answer2 = []
    for i in range(len(picture)):
        for j in picture[i]:
            answer[i] += j * k
        for _ in range(k):
            answer2.append(answer[i])
    return answer2

picture = [".xx...xx.", "x..x.x..x", "x...x...x", ".x.....x.", "..x...x..", "...x.x...", "....x...."]
k = 2

print(solution(picture, k))