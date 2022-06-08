from typing import List


def linearSearch(nums: List[int], target: int) -> int:
  n = len(nums)
  for i in range(n):
    if target == nums[i]: return i
  return -1
# Time complexity: O(n)