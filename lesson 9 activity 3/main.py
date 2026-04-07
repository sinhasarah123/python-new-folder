def incdec(n,num):
    if(n<1 or n>num):
        return
    print(n)
    incdec(n-1,num)
    print(n)
n=int(input("Enter a number: "))
incdec(n,n)