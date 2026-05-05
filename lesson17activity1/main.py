def getmaxlength(a,a_size):
    counter=0
    maximumones=0
    for i in range(0,a_size):
        if(a[i]==0):
            counter=0
        else:
            counter+=1
            maximumones=max(maximumones,counter)
    return maximumones
a=[1,1,0,1,0,1,1,1,1,1,0]
a_size=len(a)
print("maximum count of consecutive ones is...",getmaxlength(a,a_size))