def zerosattheend(a,a_size):
    zero=0
    notzero=0
    while(notzero!=a_size):
        if a[notzero]!=0:
            a[notzero],a[zero]=a[zero],a[notzero]
            zero+=1
        notzero+=1
a=[2,0,9,12,0,9,0,11,0,1]
a_size=len(a)
print(a)
zerosattheend(a,a_size)
print("After pushing zeros to the last")
print(a)