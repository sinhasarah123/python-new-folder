def reversenumber(number):
    if ( number > 0):
        last= number % 10
        if(number//10 > 0):
            current=reversenumber((int)(number/10))
            return last*pow(10,len(str(current)))+current
    return number
n=int(input("enter your number or numbers:"))
print("reversed:",reversenumber(n))