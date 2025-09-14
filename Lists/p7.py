# Rotate a list by k positions

element = [1, 2, 3, 4, 5]
k = 2
length = len(element)
k = k % length
restored = element[-k:] + element[:-k]
print(restored)   