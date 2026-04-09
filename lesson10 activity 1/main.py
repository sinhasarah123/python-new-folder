def checksorted(a):
    lenght = len(a)
    if lenght == 1 or lenght == 0:
        return True
    return a[0] <= a[1] and checksorted(a[1:])
a=[1,2,3,4,5,8,1]
if checksorted(a):
    print("\n yes array sorted")
else:
    print("\n no array not sorted")