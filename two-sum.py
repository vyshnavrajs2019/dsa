def two_sum(nums, k):
  for i in range(len(nums)):
    for j in range(i + 1,len(nums)):
      pair_sum = nums[i] + nums[j]
      if (pair_sum == k):
        return True
  return False