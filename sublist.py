list=[[1,2,3],[4,5,6],[7,8,9]]
max=0
for i in list:
    sum=0
    for j in i:
        sum +=j
    if(sum > max):
        max = sum
    c = i
print(c)
