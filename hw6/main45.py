A = int(input("Enter A as 0 or 1: "))
B = int(input("Enter B as 0 or 1: "))
C = int(input("Enter C as 0 or 1: "))

# Step by step
part1 = A and B
part2 = B and C

D = part1 or part2

print("Output D =", int(D))