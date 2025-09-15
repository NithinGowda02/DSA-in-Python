# Generate all permuatations of a List. 

from itertools import permutations

nums = [1, 2, 3, 4]
all_perms = list(permutations(nums))
print(all_perms)