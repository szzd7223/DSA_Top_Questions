def longest_mountain_in_array(arr):
    result = 0

    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            l=r=i

            while l>0 and arr[l] > arr[l-1]:
                l -= 1
            
            while r<len(arr) and arr[r] > arr[r+1]:
                r += 1

            result = max(result, r-l+1)

    return result

arr = [2,1,4,7,3,2,5]

print(longest_mountain_in_array(arr))
        