def selection_sort(arr):
    ln = len(arr)
    for x in range(ln):
        min_index = x

        for y in range(x+1, ln):
            if arr[y] < arr[min_index]:
                min_index = y
        arr[x],arr[min_index] = arr[min_index], arr[x]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

sorted_list = selection_sort(arr)
print(f"Here's the sorted list: {sorted_list}")