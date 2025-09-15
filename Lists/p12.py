# From a list, find all pairs that add up to a target.

nums = [2, 7, 17, 13, 11, -2]
target = 15

result = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if (nums[i] + nums[j]) == target:
            result.append([nums[i], nums[j]])

print(f"Final Result >> {result} ")