a = [0,4,2,0,1,8,0,5]
d = [str(i)+","+str(j)for i,j in enumerate(a) if j ==0]
print(d)
a.sort()
a = list(filter(lambda x: x!=0,a))
for i in d:
    index,item = i.split(',')
    a.insert(int(index),int(item))
print(a)
