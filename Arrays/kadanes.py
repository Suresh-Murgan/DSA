a=[1,-2,1,4,6,-4,1]
maxSum=0
curSum=0
for i in range(len(a)):
    curSum+=a[i]
    if curSum>maxSum:
        maxSum=curSum  
    if curSum<0:
        curSum=0
print(maxSum)      
            
        
    