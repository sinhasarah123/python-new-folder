def arraytotalsum(a):
    length=len(a)
    if length==1:
        return a[0]
    return a[0] + arraytotalsum(a[1:])
a=[1,2,3,4,5]
print(arraytotalsum(a))