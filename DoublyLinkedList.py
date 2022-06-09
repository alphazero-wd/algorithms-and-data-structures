from typing import Optional

class ListNode:
  def __init__(self, val: int) -> None:
    self.val: int = val
    self.prev: Optional[ListNode] = None
    self.next: Optional[ListNode] = None
  
class DoublyLinkedList:
  def __init__(self) -> None:
    self.head: Optional[ListNode] = None
    self.tail: Optional[ListNode] = None
  
  def insert_head(self, val: int):
    if not self.head: 
      self.head = ListNode(val)
      self.tail = self.head
      return
    old_head = self.head
    self.head = ListNode(val)
    self.head.next = old_head
    old_head.prev = self.head
  
  def insert_tail(self, val: int):
    if not self.head:
      self.head = ListNode(val)
      self.tail = self.head
      return
    old_tail = self.tail
    self.tail = ListNode(val)
    self.tail.prev = old_tail
    old_tail.next = self.tail
  
  def delete_head(self) -> Optional[int]:
    if not self.head: return
    old_head = self.head
    if self.head is self.tail:
      self.head = self.tail = None
    self.head = self.head.next
    self.head.prev = None
    return old_head
  
  def delete_tail(self) -> Optional[int]:
    if not self.head: return
    old_tail = self.tail
    if self.head is self.tail:
      self.head = self.tail = None
    self.tail = self.tail.prev
    self.tail.next = None
    return old_tail
  
  def contains(self, val: int) -> bool:
    cur = self.head
    while cur:
      if cur.val == val: return True
      cur = cur.next
    return False

  def print_dll(self) -> str:
    cur = self.head
    path = ''
    while cur:
      path += str(cur.val) + ' ⇆ '
      cur = cur.next
    path += 'None'
