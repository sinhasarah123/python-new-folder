a = [1, 1, 0, 1, 1, 1, 0, 1]
max_count = 0
count = 0
for num in a:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0
print("Longest consecutive 1s:", max_count)