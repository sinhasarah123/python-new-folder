arr = [0,1,1,0,0,0,1,1]

for i in range(1, len(arr)):
    
    if arr[i] != arr[i-1]:
        
        if arr[i] != arr[0]:
            print("From", i, "to", end=" ")
        else:
            print(i-1)

if arr[-1] != arr[0]:
    print(len(arr)-1)