def solution(todo_list, finished):
    answer = []
    for idx, i in enumerate(finished):
        print("i=", i, "idx=", idx)
        if i == False:
            answer.append(todo_list[idx])
    return answer

todo_list = ["problemsolving", "practiceguitar", "swim", "studygraph"]
finished = [True, False, True, False]
print(solution(todo_list, finished))