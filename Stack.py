class Stack:
  def __init__(self) -> None:
    self.items = []
  
  def push(self, val: int) -> None: 
    self.items.append(val)

  def size(self) -> int:
    return len(self.items)

  def pop(self) -> int:
    if not self.is_empty():
      return self.items.pop()
  
  def is_empty(self) -> bool:
    return self.size() == 0
  
  def peek(self) -> int:
    if not self.is_empty():
      return self.items[-1]

  def contains(self, val) -> bool:
    while not self.is_empty():
      if self.pop() == val: return True
    return False
  
  def access(self, index):
    while not self.is_empty():
      popped = self.pop()
      if index == 0: return popped
      index -= 1