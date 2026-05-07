a = [4,9,234,1,4,82,234,67]

minimum = a[0]
maximum = a[0]

for num in a:
    if num < minimum:
        minimum = num
if num > maximum:
        maximum = num
print(maximum - minimum)