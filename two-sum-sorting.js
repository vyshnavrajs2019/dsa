function twoSum(nums, k) {
  nums.sort();
  let lp = 0;
  let rp = nums.length - 1;
  while (lp < rp) {
    const sum = nums[lp] + nums[rp];
    if (sum === k) return true;
    else if (sum < k) lp += 1;
    else rp -= 1;
  }
  return false;
}
