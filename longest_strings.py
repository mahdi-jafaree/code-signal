result = []
array = [
 "yely", 
 "varennyky","ksdfkdjfk"]
max_length = 0
for i in array:
    if(len(i)>max_length):
        max_length = len(i)
        result = [i]
    elif (len(i)== max_length):
        result.append(i)
    else:
        result = list(filter(lambda r: len(r)>=max_length,result))
print(result)
