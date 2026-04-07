def headrec(n,num):
    if n > num:
        return
    headrec(n+1,num)
    print(n)
n = int(input("Enter a number: "))

headrec(1,n)
