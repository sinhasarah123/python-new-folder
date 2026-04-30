
def calculate_water(arr, a_size):
    lefttallest=[0]* a_size
    righttallest=[0]* a_size
    water=0
    lefttallest[0]=arr[0]
    for i in range(1,a_size):
        lefttallest[i]=max(lefttallest[i-1],arr[i])
    righttallest[a_size-1]=arr[a_size-1]
    for i in range(a_size-2,-1,-1):
        righttallest[i]=max(righttallest[i+1],arr[i])
    for i in range(0,a_size):
        water += min(lefttallest[i],righttallest[i]) - arr[i]
    return water
arr=[0,1,0,2,1,0,1,3,2,1,2,1]
bars=len(arr)
print("water thats been trapped is..:",calculate_water(arr, bars))