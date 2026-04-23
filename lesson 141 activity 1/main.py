def arraymean(arr,arr_size):
    totalsum=0
    for i in range (0,arr_size):
        totalsum += arr[i]
    return float(totalsum) / arr_size
def arraymedian(arr,arr_size):
    sorted(arr)
    if arr_size % 2 !=0:
        return float(arr[int(arr_size/2)])
    return float((arr[int(arr_size/2)-1] + arr[int(arr_size/2)])/2)
arr=[1,2,3,4,5]
arr_size=len(arr)
print("Mean is ",arraymean(arr,arr_size))
print("Median is ",arraymedian(arr,arr_size))