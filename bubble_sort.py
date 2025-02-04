# Bubble Sort Algorithm
def bubble(list1):
    n = len(list1)
    for i in range(n):
        for j in range(0, n-i-1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

list1 = [9, 6, 3, 5, 2, 8, 7, 4, 1]

print("Unsorted list: ", list1)
print("Sorted list: ", bubble(list1))