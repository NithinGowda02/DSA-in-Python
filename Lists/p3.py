# Reverese a List without using reverse() or slicing.

element = [12, 23, 32, 22, 45, 8]
sorted_element = []
for i in range(len(element)-1, -1, -1):
    sorted_element.append(element[i])

print(sorted_element)    