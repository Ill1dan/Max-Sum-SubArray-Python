# Time Complexity - O(nlogn)

def maxCrossing(arr, l, h, m):

    sum = 0
    left_sum = -float("inf")
    for i in range(m, l - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum

    sum = 0
    right_sum = -float("inf")
    for j in range(m, h + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum

    return max(left_sum + right_sum - arr[m], left_sum, right_sum)



def maxCrossingSubArray(arr, l, h):
    if l > h:
        return -float("inf")
    if l == h:
        return arr[l]
    m = (l + h) // 2

    return max(maxCrossingSubArray(arr, l, m - 1), maxCrossingSubArray(arr, m + 1, h), maxCrossing(arr, l, h, m))

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
print(maxCrossingSubArray(arr, 0, len(arr) - 1))