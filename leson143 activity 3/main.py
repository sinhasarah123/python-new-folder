def print2largest(a,a_size):
    largest=secondlargest=-999999999
    for i in range (a_size):
        if a[i]>largest:
            secondlargest=largest
            largest=a[i]
        elif a[i]>secondlargest and a[i]!=largest:
            secondlargest=a[i]
    print("The second largest number is",secondlargest)
a=[10,20,4,45,99]
a_size=len(a)
print2largest(a,a_size)