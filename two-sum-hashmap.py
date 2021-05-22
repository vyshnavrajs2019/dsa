def two_sum(nums, k):
  hashmap = {}
  for num in nums:
    required = k - num
    if required in hashmap:
      return True
    hashmap[num] = True
  return False
  