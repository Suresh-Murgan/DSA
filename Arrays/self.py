def brute(a):
    n=len(arr)
    pre=[1]*n
    prefix=1
    for i in range(len(a)):
     pre[i]=prefix*a[i]
    return pre
    
    
arr=[1,2,3,4]
)
print(brute(arr))