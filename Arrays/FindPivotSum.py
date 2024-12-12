# LeetCode 724 -Find the Pivot Element 
a=[1,7,3,6,5,6]
tsum=sum(a)
lsum=0
for i in range(len(a)):
    rsum=tsum-lsum-a[i]
    if lsum==rsum:
        print(i)
    lsum+=a[i]