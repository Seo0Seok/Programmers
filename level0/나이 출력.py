import random

def solution(age):
    global year
    result = year - age + 1
    return result

year = 2022
age = random.sample(range(1, 121), 1)[0]
result = solution(age)
print(f"{year}년 기준 {age}살이므로 {result}년생입니다.")