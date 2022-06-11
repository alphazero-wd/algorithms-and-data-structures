class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, val: int) -> None:
    self.items.append(val)

  def size(self) -> int: return len(self.items)

  def dequeue(self) -> int:
    if not self.is_empty():
      return self.items.pop(0)

  def is_empty(self) -> bool:
    return self.size() == 0

  def peek(self) -> int:
    if not self.is_empty():
      return self.items[0]

  def contains(self, val: int) -> bool:
    while not self.is_empty():
      if self.dequeue() == val: return True      
    return False
  
  def access(self, index: int) -> int:
    while not self.is_empty():
      front = self.dequeue()
      if index == 0: return front
      index -= 1