import re
string = "foo(bar(baz))blim"
def solution (inputString):
    array = re.findall(r"\([a-z]*\)",inputString)
    result = re.sub(r"\([a-z]*\)","-",inputString)
    array = [(lambda i: re.sub(r"[\(\)]","",i))(i)[::-1] for i in array ]
    for i in array:
        result = result.replace("-",i,1)    
    if re.findall(r"\([a-z]*\)",result): return solution(result)
    return result

print(solution("aba(bar(baz))blim"))

#### Top solution
#### def solution(s):
    # for i in range(len(s)):
    #     if s[i] == "(":
    #         start = i
    #     if s[i] == ")":
    #         end = i
    #         return solution(s[:start] + s[start+1:end][::-1] + s[end+1:])
    # return s