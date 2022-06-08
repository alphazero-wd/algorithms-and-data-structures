from typing import List


def bubbleSort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n):
    for j in range(i):
      if nums[i] < nums[j]:
        nums[i], nums[j] = nums[j], nums[i]
  return nums
# Time complexity: O(n^2)
# Space complexity: O(1)