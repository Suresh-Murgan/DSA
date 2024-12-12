# LeetCode-766 
a=[[1,2,3,4],[5,1,2,3],[9,5,1,2]]
row=len(a)
col=len(a[0])
for i in range(row-1):
    for j in range(col-1):
        if(a[i][j]!=a[i+1][j+1]):
            print("False")
            exit()
print("True")
    