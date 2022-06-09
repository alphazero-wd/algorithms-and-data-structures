from typing import List, Optional
class Heap:
  def __init__(self) -> None:
    self.items: List[int] = [None]
  
  def size(self) -> int:
    return len(self.items)
  
  def is_empty(self) -> bool:
    return self.size() <= 1
  
  def peek(self) -> Optional[int]:
    if not self.is_empty(): return self.items[1]

class MaxHeap(Heap):
  def __init__(self) -> None:
    super().__init__()

  def swim(self, i: int) -> None:
    while i // 2 > 0 and self.items[i // 2] < self.items[i]:
      self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
      i //= 2
    
  def sink(self, i: int) -> None:
    while 2 * i < self.size():
      j = 2 * i
      if j + 1 < self.size() and self.items[j] < self.items[j + 1]: j += 1
      if self.items[i] >= self.items[j]: break
      self.items[j], self.items[i] = self.items[i], self.items[j]
      i = j
  
  def insert(self, val: int) -> None:
    self.items.append(val)
    self.swim(self.size() - 1)
  
  def del_max(self) -> int:
    self.items[1], self.items[-1] = self.items[-1], self.items[1]
    max_item = self.items.pop()
    self.sink(1)
    return max_item
    
  def heapsort(self) -> List[int]:
    res = []
    while not self.is_empty():
      res.insert(0, self.del_max())
    return res

class MinHeap(Heap):
  def __init__(self) -> None:
    super().__init__()

  def swim(self, i: int) -> None:
    while i // 2 > 0 and self.items[i // 2] > self.items[i]:
      self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]
      i //= 2
    
  def sink(self, i: int) -> None:
    while 2 * i < self.size():
      j = 2 * i
      if j + 1 < self.size() and self.items[j] > self.items[j + 1]: j += 1
      if self.items[i] <= self.items[j]: break
      self.items[j], self.items[i] = self.items[i], self.items[j]
      i = j
  
  def insert(self, val: int) -> None:
    self.items.append(val)
    self.swim(self.size() - 1)
  
  def del_min(self) -> int:
    self.items[1], self.items[-1] = self.items[-1], self.items[1]
    min_item = self.items.pop()
    self.sink(1)
    return min_item

  def heapsort(self) -> List[int]:
    res = []
    while not self.is_empty():
      res.append(self.del_min())
    return res

# Time complexity
# Operation           Analysis
# Insertion           O(log2(n))
# Deletion            O(log2(n))
# Peek                O(log2(n))
# Heapsort            O(nlog2(n))