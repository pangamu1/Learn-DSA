# Selection Sort Algorithm
def selection_sort(list1):
    n = len(list1)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if list1[j] < list1[min_index]:
                min_index = j
        list1[i], list1[min_index] = list1[min_index], list1[i]
    return list1

list1 = [9, 6, 3, 5, 2, 8, 7, 4, 1]

print("Unsorted list: ", list1)
print("Sorted list: ", selection_sort(list1))