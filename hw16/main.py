a = [6,4,9,4,7,2,3,4,2,52]

max_len = 1
current_len = 1

for i in range(1, len(a)):
    if (a[i] % 2) != (a[i-1] % 2):
        current_len += 1
        max_len = max(max_len, current_len)
    else:
        current_len = 1

print(max_len)