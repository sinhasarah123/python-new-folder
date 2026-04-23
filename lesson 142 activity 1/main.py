def minelement(a, size):
    temp =a[0]
    for i in range (1,size):
        temp=min(temp,a[i])
    return temp
def maxlement(a, size):
    temp =a[0]
    for i in range (1,size):
        temp=max(temp,a[i])
    return temp
a=[1,2,3,4,5]
size = len(a)
print("Minimum element is ", minelement(a,size))
print("Maximum element is ", maxlement(a,size))
