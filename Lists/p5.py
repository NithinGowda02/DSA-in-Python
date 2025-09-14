# Remove duplicate while keeping order. 

elements = [12, 34, 23, 56, 78, 66, 12, 23, 66, 12]
unique = []

for i in elements:
    if i not in unique:
        unique.append(i)
print("List After removing Duplicate elements..>> ")
print(unique)        
