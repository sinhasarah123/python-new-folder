
num = int(input("Enter a number: "))
binary = bin(num)[2:]
reversed_binary = binary[::-1]
new_number = int(reversed_binary, 2)
print("Binary:", binary)
print("Reversed Binary:", reversed_binary)
print("New Number:", new_number)