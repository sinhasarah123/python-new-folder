def find_missing(arr, n):
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual



arr = [1, 2, 4, 5]
n = 5
print(find_missing(arr, n))  