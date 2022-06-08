class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, val):
    self.items.append(val)
  
  def dequeue(self):
    if not self.is_empty():
      return self.items.pop(0)

  def is_empty(self):
    return len(self.items) == 0

  def peek(self):
    if not self.is_empty():
      return self.items[0]
# Time complexity:
# Operation         Analysis
# Enqueue           O(1)
# Dequeue           O(1)
# Peek              O(1)
