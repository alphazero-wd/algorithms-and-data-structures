class Stack:
  def __init__(self) -> None:
    self.items = []
  
  def push(self, val): 
    self.items.append(val)
  
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
  
  def is_empty(self):
    return len(self.items) == 0
  
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
# Time complexity:
# Operation         Analysis
# Push              O(1)
# Pop               O(1)
# Peek              O(1)