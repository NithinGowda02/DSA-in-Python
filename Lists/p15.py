# sort element list by frequency

from collections import Counter

nums = [4, 6, 2, 6, 4, 4, 6, 2, 6, 8]
freq = Counter(nums)
result = [n for n, count in freq.most_common() for _ in range(count)]

print(result)
