# Intuition

## Problem Breakdown
A mountain array is defined as an array that increases to a peak and then decreases. The goal is to find the longest contiguous subarray that follows this pattern.

## Approach (Two Pointer)
1. Iterate through the array and identify peak elements (i.e., `arr[i-1] < arr[i] > arr[i+1]`).
2. Expand outwards from the peak:
   - Move left while elements are increasing.
   - Move right while elements are decreasing.
3. Calculate the length of the mountain and update the maximum found.
4. Return the longest mountain length or `0` if no valid mountain is found.

## Complexity Analysis
- Each element is processed at most twice (once expanding left and once expanding right).
- Time Complexity: **O(n)** (linear scan with expansion)
- Space Complexity: **O(1)** (constant space usage)

## Question Link
https://leetcode.com/problems/longest-mountain-in-array/description/