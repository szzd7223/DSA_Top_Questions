# Sliding Window Approach

The sliding window technique is an efficient way to solve problems involving contiguous subarrays or sequences. Instead of recalculating the sum or result from scratch for every window, we update it dynamically as the window moves through the array.

## Steps to Implement Sliding Window:

1. **Initialize the window** – Compute the sum for the first `k` elements.
2. **Slide the window** – Move the window one step at a time by:
   - Subtracting the element that is left behind.
   - Adding the new element entering the window.
3. **Track the maximum (or desired result)** – Update the result if the new sum is larger.

## Example : Maximum Sum of a Subarray of Size `k`

```python
# Function to find the maximum sum of a subarray of size k
def sliding_window(arr, k):
    sum = 0  # Stores the sum of the current window
    maxSum = 0  # Stores the maximum sum found
    
    # Compute the sum of the first window
    for i in range(0, k):
        sum += arr[i]
    
    l = 0  # Left boundary of the window
    r = k - 1  # Right boundary of the window

    # Slide the window across the array
    while r < len(arr) - 1:
        sum = sum - arr[l]  # Remove the element going out of the window
        l += 1  # Move left boundary forward

        r += 1  # Move right boundary forward
        sum = sum + arr[r]  # Add the new element entering the window

        maxSum = max(sum, maxSum)  # Update maxSum if a larger sum is found

    return maxSum  # Return the maximum sum found

arr = [-1, 2, 3, 3, 4, 5, -1]
k = 4
print(sliding_window(arr, k))  # Output: 15
```

### Breakdown:

- **First window (first ********`k=4`******** elements)**: `[-1, 2, 3, 3]` → Sum = `7`
- **Slide the window right**:
  - Remove `-1`, add `4` → New sum = `7 - (-1) + 4 = 12`
  - Remove `2`, add `5` → New sum = `12 - 2 + 5 = 15`
  - Remove `3`, add `-1` → New sum = `15 - 3 + (-1) = 11`
- **Maximum sum found**: `15`