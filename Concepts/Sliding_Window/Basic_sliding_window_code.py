def sliding_window(arr, k):
    sum = 0
    maxSum = 0
    for i in range(0,k):
        sum += arr[i]
    
    l = 0
    r = k-1

    while r < len(arr):
        sum = sum - arr[l]
        l+=1

        sum = sum + arr[r]
        r+=1

        maxSum = max(sum, maxSum)

    return maxSum


arr = [-1,2,3,3,4,5,-1] #output is 15 [3,3,4,5]

print(sliding_window(arr,4)) 