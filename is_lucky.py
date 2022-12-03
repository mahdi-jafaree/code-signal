def solution(n):
    l = 0
    f = 0
    for i in range(int(len(str(n))/2)):
        f += int(str(n)[i])
        l += int(str(n)[-(i+1)])
    if f == l:
        return True
    else:
        return False
print(solution(2222))
