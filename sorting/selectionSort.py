from typing import List


def selectionSort(nums: List[int]) -> List[int]:
  n = len(nums)
  for i in range(n):
    minIndex = i
    for j in range(i + 1, n):
      if nums[j] < nums[minIndex]: minIndex = j
    if i != minIndex: nums[i], nums[minIndex] = nums[minIndex], nums[i]
  return nums 
# Time complexity: O(n^2)
# Space complexity: O(1)