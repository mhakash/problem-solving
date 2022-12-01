def remove_duplicates(arr):
    l, r = 1, 1
    
    while r < len(arr):
        if arr[l-1] != arr[r]:
            arr[l] = arr[r]
            l += 1
        
        r += 1
    
    return l

print(remove_duplicates([2, 3, 3, 6, 9, 9]))