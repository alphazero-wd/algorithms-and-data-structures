from typing import Optional

class ListNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.next: Optional[ListNode] = None
  
class SinglyLinkedList:
  def __init__(self) -> None:
    self.head: Optional[ListNode] = None

  def insert_head(self, val: int):
    if not self.head: 
      self.head = ListNode(val)
      return
    old_head = self.head
    self.head = ListNode(val)
    self.head.next = old_head
  
  def delete_by_value(self, val: int):
    if not self.head: return
    if self.head.val == val:
      self.head = self.head.next
    cur = self.head
    prev: Optional[ListNode] = None
    while cur:
      if cur.val == val:
        prev.next = cur.next 
      prev = cur
      cur = cur.next

  def delete_head(self) -> int or None:
    if not self.head: return
    old_head = self.head
    self.head = self.head.next
    return old_head.val
  
  def contains(self, val: int) -> bool:
    cur = self.head
    while cur:
      if cur.val == val: return True
      cur = cur.next
    return False

  def print_sll(self) -> str:
    cur = self.head
    path = ''
    while cur:
      path += str(cur.val) + ' -> '
      cur = cur.next
    path += 'None'
    return path
# Time complexity
# n: # of nodes in a SLL
# Operation               Analysis
# Insertion at head       O(1)
# Deletion at head        O(1)
# Deletion by a value     O(n)
# Find                    O(n)