n=int(input("enteer a number:"))
def checkIfpower(n):
    if(n<-0):
        return False
    if(n==1):
        return True
    if(n%4==0):
        return checkIfpower(n//4)
    return False
if(checkIfpower (n)):
    print("power of 4")
else:
    print("not power of 4")
 