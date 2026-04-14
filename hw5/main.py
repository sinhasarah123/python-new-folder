n=int(input("enteer a number:"))
def checkIfpower(n):
    if(n<-0):
        return False
    if(n==1):
        return True
    if(n%2==0):
        return checkIfpower(n//2)
    return False
if(checkIfpower (n)):
    print("power of 2")
else:
    print("not power of 2")