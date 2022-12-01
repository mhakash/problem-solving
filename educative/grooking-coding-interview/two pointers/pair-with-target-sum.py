# arr is sorted
def pair_with_target_sum(arr, target):
    l, r = 0, len(arr) - 1
    
    while l < r:
        curr_sum = arr[l] + arr[r]
        if curr_sum == target:
            return [l, r]
        
        if target > curr_sum:
            l += 1
        else:
            r -= 1
    return [-1, -1]


print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
