# Insertion Sort Algorithm
def insertion_sort(list1):
    n = len(list1)
    
    for i in range(1, n):
        key = list1[i]
        j = i-1

        while j >= 0 and list1[j] > key:
            list1[j+1] = list1[j]
            j -= 1

        list1[j+1] = key

    return list1

list1 = [6, 3, 5, 2, 8, 7, 4, 1]
print("Unsorted list: ", list1)
print("Sorted list: ", insertion_sort(list1))