def solution(a,b):
    count = 0
    diffIndex = []
    if(len(a)!=len(b)): return False
    if(a==b): 
        return a == b
    else:
        for i,j in zip(a,b):
            if(i!=j): 
                count+=1
                diffIndex.append((i,j))
            if(count>2): return False
        if count==2:
            return diffIndex[0][0]==diffIndex[1][1] and diffIndex[0][1]==diffIndex[1][0]
        
        return False
print(solution([2,1,3],[1,2,3]))