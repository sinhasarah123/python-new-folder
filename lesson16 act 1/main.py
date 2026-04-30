def calculateprofits(arr,arr_size):
    profit=0
    for i in range(1,arr_size):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
prices=[7,1,5,3,6,4]
profit=calculateprofits(prices,len(prices))
print(profit)