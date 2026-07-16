# set matrix to zero
max=[[1,1,1],
     [1,0,1],
     [1,1,1]]
rows=len(max)
cols=len(max[0])
row=[False]*rows
col=[False]*cols
for i in range(rows):
    for j in range(cols):
        if max[i][j]==0:
            row[i]=True
            col[j]=True
for i in range(rows):
    for j in range(cols):
        if row[i] or col[j]:
            max[i][j]=0
print(max)
