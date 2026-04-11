def arrayLenghtRecursive(arr):
    if arr == []:
        return 0
    
        return 1 + arrayLenghtRecursive(arr[1:])

my_list = [1, 2, 3, 4, 5]

print(arrayLenghtRecursive(my_list))