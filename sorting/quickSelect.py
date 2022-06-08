from typing import List

def select(nums: List[int], left: int, right: int, k: int) -> int:
  pivotIndex = partition(nums, left, right)
  # The pivot is in its final sorted position
  if k == pivotIndex: return nums[k]
  elif k < pivotIndex: return select(nums, left, pivotIndex - 1, k)
  else: return select(nums, pivotIndex + 1, right, k)

def partition(nums: List[int], left: int, right: int) -> int:
  i, j = left - 1, right + 1
  while True:
    i += 1 
    while nums[i] < nums[left]:
      i += 1
      if i == right: break
    j -= 1
    while nums[j] > nums[left]:
      j -= 1
      if j == left: break
    if i >= j: break
    nums[i], nums[j] = nums[j], nums[i]
  nums[left], nums[j] = nums[j], nums[left]
  return j

def findKthLargest(nums: List[int], k: int) -> int:
  n = len(nums)
  k = n - k
  return select(nums, 0, n - 1, k)
# Time complexity: O(n), worst case O(n^2)