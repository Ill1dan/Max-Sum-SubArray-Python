﻿# Max Sum SubArray Python

## What is it?
        This is the maximum possible sum of consecutive sub-array. This problem can easily be solved in O(nlogn) 
        Time by applying the Divide and Conquer Rule. Kadandes's Algorithm solves this problem in O(n) Time.

## Divide And Conquer Approach - O(nlogn)

### Step - 1
        In the maxCrossingSubArray() function we recursively solve the left sum, right sum and crossing sum and 
        finally return the max(left sum, right sum and crossing sum).
```python
    def maxCrossingSubArray(arr, l, h):
        if l > h:
            return -float("inf")

        if l == h:
            return arr[l]
            
        m = (l + h) // 2

        return max(maxCrossingSubArray(arr, l, m - 1), maxCrossingSubArray(arr, m + 1, h), maxCrossing(arr, l, h, m))
```
### Step - 2
        In the maxCrossing() function we find the sum the crossing array. Then find the max(crossing sum, left sum and right sum).

        We find the max sum in left side of the sub-array from the mid point.
```python
    sum = 0
    left_sum = -float("inf")
    for i in range(m, l - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
```
        Then find the max sum in right side of the sub-array from the mid point.
```python
    sum = 0
    right_sum = -float("inf")
    for j in range(m, h + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
```
        Finally, we return the max(crossing sum, left sum and right sum).


## Kadandes's Algorithm - O(n)

### Step - 1 
        In this algorithm we will iterate through the array and keep updating the temp_sum and sum. We first set the sum to the 
        lowest possible value. After enter the loop we add each index with the temp_sum. If temp_sum greater than the sum we 
        make the sum = temp_sum, as now temp_sum is the max. 

### Step - 2
        Now if the temp_sum is less than 0 we will not carry it to the next iteration, because if we carry negative number and add
        the next index the sum will decrease instead of increase. So, we will only carry the positive number. Finally, we will 
        return the sum when the loop ends.
