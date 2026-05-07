def kadane(a):
    n=len(a)
    maxsofar=0
    maxendinghere=0
    for i in range(0,n):
        maxendinghere=maxendinghere+a[i]
        if(maxendinghere<0):
            maxendinghere=0
        if(maxsofar<maxendinghere):
            maxsofar=maxendinghere
    return maxsofar
def maxcircularsum(a):
    n=len(a)
    max_kadane=kadane(a)
    max_wrap=0
    for i in range(0,n):
        max_wrap=max_wrap+a[i]
        a[i]=-a[i]
    max_wrap=max_wrap+kadane(a)
    if max_wrap > max_kadane:
        return max_wrap
    return max_kadane
a=[11,10,-20,5,-3,-5,8,-13,10]
print("the maximum crcular sum is:",maxcircularsum(a))