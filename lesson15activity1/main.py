def reverse(a,a_size,n):
    temp=0
    while(temp<a_size):
        start=temp
        end=min(temp+n-1,a_size-1)
        # Reverse the subarray from start to end
        while(start<end):
            a[start],a[end]=a[end],a[start]
            start+=1
            end-=1
        temp+=n
a=[5,3,2,23,6,9,8]
n=2
a_size=len(a)
reverse(a,a_size,n)
for i in range(0,a_size):
    print(a[i],end=" ")