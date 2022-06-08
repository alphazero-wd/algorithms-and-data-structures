from typing import List


def insertionSort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n):
    for j in range(i, 0, -1):
      if nums[j] < nums[j - 1]:
        [nums[j], nums[j - 1]] = [nums[j - 1], nums[j]]
  return nums
# Time complexity: O(n^2)
# Space complexity: O(1)