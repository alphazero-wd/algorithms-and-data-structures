from typing import List

def select(nums: List[int], left: int, right: int, k: int) -> int:
  pivotIndex = partition(nums, left, right)
  # The pivot is in its final sorted position
  if k == pivotIndex: return nums[k]
  elif k < pivotIndex: return select(nums, left, pivotIndex - 1, k)
  else: return select(nums, pivotIndex + 1, right, k)

def partition(nums: List[int], left: int, right: int) -> int:
  mid = (left + right) // 2
  pivot = nums[mid]
  nums[mid], nums[right] = nums[right], nums[mid]
  for i in range(left, right + 1):
    if nums[i] < pivot:
      nums[i], nums[left] = nums[left], nums[i] 
      left += 1
  nums[right], nums[left] = nums[left], nums[right]
  return left

def findKthLargest(nums: List[int], k: int) -> int:
  n = len(nums)
  k = n - k
  return select(nums, 0, n - 1, k)