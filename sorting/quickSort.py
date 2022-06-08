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
  i, j = low - 1, high + 1
  while True:
    i += 1 
    while nums[i] < nums[low]:
      i += 1
      if i == high: break
    j -= 1
    while nums[j] > nums[low]:
      j -= 1
      if j == low: break
    if i >= j: break
    nums[i], nums[j] = nums[j], nums[i]
  nums[low], nums[j] = nums[j], nums[low]
  return j
print(quickSort([3, 2, 1, 5, 6, 4]))
# Time complexity: O(nlog2(n)), O(n^2) if we choose a bad pivot (but it rarely happens)
# Space complexity: O(log2(n))