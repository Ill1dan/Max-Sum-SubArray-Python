# Time Complexity - O(n)

def maxCrossingSubArray(arr):
    temp_Sum = 0
    sum = -float("inf")

    for i in arr:
        temp_Sum += i

        if temp_Sum > sum:
            sum = temp_Sum

        if temp_Sum < 0:
            temp_Sum = 0

    return sum

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print(maxCrossingSubArray(arr))
