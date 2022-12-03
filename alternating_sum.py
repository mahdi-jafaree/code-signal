def solution(a):
    return [sum([a[i] for i in range( len(a)) if i%2==0]),sum([a[i] for i in range( len(a)) if i%2!=0])]

# def solution(a):
#     return [sum(a[::2]),sum(a[1::2])]