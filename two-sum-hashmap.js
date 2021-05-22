function twoSum(nums, k) {
  const hashMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const required = k - nums[i];
    if (hashMap.has(required)) return true;
    hashMap.set(nums[i], true);
  }
  return false;
}
