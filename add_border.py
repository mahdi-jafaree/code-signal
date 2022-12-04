def solution(picture):
    vertical = "*"*(len(picture[0])+2)
    result = [vertical,*picture,vertical]
    for i in range(len(result[1:-1])):
        result[i+1] = "*"+ result[i+1]+"*"
    return result

print(solution(["abc","abcdd"]))