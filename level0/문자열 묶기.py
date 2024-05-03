def solution(strArr):
    list1 = [0] * len(strArr)
    for i in strArr:
        list1[len(i)] += 1
    return max(list1)

strArr = ["a","bc","d","efg","hi"]

print(solution(strArr))
