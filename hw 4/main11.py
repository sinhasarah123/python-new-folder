def take_input():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Stopped (negative number entered)")
        return
    else:
        take_input()

take_input()