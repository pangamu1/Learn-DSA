import random

lst = [random.randint(50,70) for x in range(10)]

def duplicates(lst):
    seen = set()
    dupes = set()

    for x in lst:
        if x in seen:
            dupes.add(x)
        else:
            seen.add(x)
    return list(dupes)

def count_duplicates(lst):
    dupes = {}

    for x in lst:
        dupes[x] = dupes.get(x,0) + 1
    return {x: y for x,y in dupes.items() if y > 1}

print(f"Original list: {lst}\nDuplicates: {duplicates(lst)}\nCount of Duplicates:{count_duplicates(lst)}")