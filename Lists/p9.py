# convert [[1, 2], [3, 4], [5, 6]] -> [1, 2, 3, 4, 5, 6]

nested = [[1, 2], [3, 4], [5, 6]]
new_list = []
for nest in nested:
    for item in nest:
        new_list.append(item)
print(new_list)        
