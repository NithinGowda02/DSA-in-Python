elements = [4, 5, 2, 20, 10, 15, 8]
target = 33
n = len(elements)
found = False

for start in range(n):
    curr_sum = 0
    for end in range(start, n):
        curr_sum += elements[end]
        if curr_sum == target:
            print(f"SubArray Found >> {elements[start:end+1]}")
            found = True
            break
        if found:
            break
