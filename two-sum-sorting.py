def two_sum(nums, k):
  nums.sort()
  lp = 0
  rp = len(nums) - 1
  while lp < rp:
    pair_sum = nums[lp] + nums[rp]
    if pair_sum == k:
      return True
    elif pair_sum < k:
      lp += 1
    else:
      rp -= 1
  return False
  