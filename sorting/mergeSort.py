from typing import List


def mergeSort(nums: List[int]) -> List[int]:
  n = len(nums)
  aux = [None] * n
  sort(nums, 0, n - 1, aux)
  return nums

def sort(nums: List[int], low: int, high: int, aux: List[int]) -> List[int]:
  if low >= high: return 
  mid = (low + high) // 2
  sort(nums, low, mid, aux)
  sort(nums, mid + 1, high, aux)
  merge(nums, low, high, mid, aux)

def merge(nums: List[int], low: int, high: int, mid: int, aux: List[int]) -> None:
  for k in range(low, high + 1):
    aux[k] = nums[k]
  
  left, right = low, mid + 1
  for i in range(low, high + 1):
    if left > mid: 
      nums[i] = aux[right]
      right += 1
    elif right > high:
      nums[i] = aux[left] 
      left += 1
    elif aux[left] < aux[right]:
      nums[i] = aux[left]
      left += 1
    else:
      nums[i] = aux[right]
      right += 1
# Time complexity: O(nlog2(n))
# Space complexity: O(n) 