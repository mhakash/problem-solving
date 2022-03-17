# binary search with left most or rigth most element
def binary_search(arr, item, left=True):
    low = 0
    high = len(arr) - 1
    index = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            if left:
                index = mid
                high = mid - 1
            else:
                index = mid
                low = mid + 1
        elif arr[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    return index


a = [1, 4, 6, 7, 8, 8, 8, 9, 15, 20, 23]
item = 8
left_index = binary_search(a, item, True)
right_index = binary_search(a, item, False)
total_items = 0

if left_index != -1:
    total_items = right_index - left_index + 1

print(total_items)
