def solution(numbers):
    number1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number2 = [0,1,2,3,4,5,6,7,8,9]

    for i in range(len(number1)):
        if number1[i] in numbers:
            numbers = numbers.replace(number1[i], str(number2[i]))
    return int(numbers)

numbers = "onetwothreefourfivesixseveneightnine"
print(solution(numbers))