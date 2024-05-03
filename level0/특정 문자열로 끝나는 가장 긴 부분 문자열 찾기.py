def solution(myString, pat):
    a = myString[::-1].index(pat[::-1])       
    return myString[:len(myString) - a]

myString = "AAAAaaaa"
pat = "a"

print(solution(myString, pat))

# a = myString[::-1].index(pat[::-1])
# print("myString[::-1]=", myString[::-1])
# print("len(myString) - a=", len(myString) - a)
# print(myString[:len(myString) - a])