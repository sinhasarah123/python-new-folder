
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1



def recursive_binary_search(arr, low, high, target):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    else:
        return recursive_binary_search(arr, low, mid - 1, target)



seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seat_no = int(input("Enter seat number to search: "))


result1 = iterative_binary_search(seats, seat_no)

if result1 != -1:
    print("Iterative Search: Seat found at index", result1)
else:
    print("Iterative Search: Seat not found")


result2 = recursive_binary_search(seats, 0, len(seats) - 1, seat_no)

if result2 != -1:
    print("Recursive Search: Seat found at index", result2)
else:
    print("Recursive Search: Seat not found")



print("\nComplexity Comparison")
print("Iterative Binary Search:")
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")

print("\nRecursive Binary Search:")
print("Time Complexity: O(log n)")
print("Space Complexity: O(log n) due to recursion stack")