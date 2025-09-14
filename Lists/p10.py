# intersection and union of 2 Lists

list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 7, 8, 9]

#Intersection

intersection = [x for x in list1 if x in list2]
print(intersection)

#Union

union = [list1.append(x) for x in list2 if x not in list1]
print(list1)
