def find_paths(i, j, n, m, path=""):
    if i == n - 1 and j == m - 1:
        print(path)
        return
    
    if i < n - 1:
        find_paths(i + 1, j, n, m, path + "d")
    
    if j < m - 1:
        find_paths(i, j + 1, n, m, path + "r")


# input
n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

find_paths(0, 0, n, m)