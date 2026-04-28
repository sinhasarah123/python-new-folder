def leader(a, a_size):
    currentmax = a[a_size - 1]
    print(currentmax)
    for i in range(a_size - 2, -1, -1):
        if currentmax<a[i]:
            print(a[i])
            currentmax = a[i]
a=[1,243,5,11,9,8,7,6,5,4,3,2,1]
leader(a,len(a))