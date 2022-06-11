from typing import List

def quickSort(nums: List[int]) -> List[int]:
  n = len(nums)
  sort(nums, 0, n - 1)
  return nums

def sort(nums: List[int], low: int, high: int) -> List[int]:
  if low >= high: return
  index = partition(nums, low, high)
  sort(nums, low, index - 1)
  sort(nums, index + 1, high)

def partition(nums: List[int], low: int, high: int) -> int:
  mid = (low + high) // 2
  pivot = nums[mid]
  nums[high], nums[mid] = nums[mid], nums[high]
  i = low 
  for j in range(low, high):
    if nums[j] < pivot:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
  nums[i], nums[high] = nums[high], nums[i]
  return i