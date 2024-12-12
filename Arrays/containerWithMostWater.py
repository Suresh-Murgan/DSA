def findAreaBrute(a):
    n=len(a)
    maxi=0
    for i in range(n):
        for j in range(i+1,n):
            b=j-i
            l=min(a[i],a[j])
            area=l*b
        maxi=max(maxi,area)
    return maxi
    
def findAreaOpti(a):
     n=len(a)
     l=0
     r=n-1
     maxi=0
     while(l< r):
         b=r-l
         le=min(a[l],a[r])
         area=le*b
         maxi=max(maxi,area) 
         if(a[l]>a[r]):
             r-=1
         else:
             l+=1
     return maxi
            
a=[1,8,6,2,5,4,8,3,7]
print(findAreaOpti(a))