# Count how many times a given element appears.

elements = [12, 34, 56, 23, 34, 78, 34, 78]
target = 34
count = 0

for i in elements:
    if i == target:
        count += 1
print(f"{target} Appeared {count} times.")        
