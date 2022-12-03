matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]

total = 0
for i in list(zip(*matrix)):
    for j in i:
        if(j ==0):
            break
        total+=j


print(total)