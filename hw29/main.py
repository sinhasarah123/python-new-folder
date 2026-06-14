a = 10
b = 20

a = a + b
b = a - b
a = a - b

print("After swap:", a, b)


x = 5
y = 7

x = x ^ y
y = x ^ y
x = x ^ y

print("After XOR swap:", x, y)


num = 8
print("Double:", num << 1)


a = -10
b = 20

if (a ^ b) < 0:
    print("Different signs")
else:
    print("Same signs")


dividend = 20
divisor = 4

quotient = 0
temp = dividend

while temp >= divisor:
    temp -= divisor
    quotient += 1

print("Quotient:", quotient)