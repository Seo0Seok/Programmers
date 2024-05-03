def solution(myStr):
    answer = ["a", "b", "c"]

    for i in answer:
        myStr = myStr.replace(i, ' ')
    myStr = myStr.split()
    
    if len(myStr) == 0:
        return ["EMPTY"]
    return myStr

myStr = "baconlettucetomato"
myStr = myStr.split("a|b|c")
print(myStr)
# print(solution(myStr))