from typing import Optional
from queue import Queue

class TreeNode:
  def __init__(self, val: int) -> None:
    self.val = val
    self.left: Optional[TreeNode] = None
    self.right: Optional[TreeNode] = None
  
class BinaryTree(object):
  def __init__(self) -> None:
    self.root: Optional[TreeNode] = None

  def inorder(self) -> None:
    def traverse(root: Optional[TreeNode]):
      if not root: return ''
      traverse(root.left)
      print(root.val, end=' ')
      traverse(root.right)
    traverse(self.root)
  
  def preorder(self) -> None:
    def traverse(root: Optional[TreeNode]):
      if not root: return ''
      print(root.val, end=' ')
      traverse(root.left)
      traverse(root.right)
    traverse(self.root)

  def postorder(self) -> None:
    def traverse(root: Optional[TreeNode]):
      if not root: return ''
      traverse(root.left)
      traverse(root.right)
      print(root.val, end=' ')
    traverse(self.root)
  
  def level_order(self) -> None:
    if not self.root: return
    queue: Queue[TreeNode] = Queue()
    queue.put(self.root)
    while not queue.empty():
      cur = queue.get()
      print(cur.val, end=" ")
      if cur.left: queue.put(cur.left)
      if cur.right: queue.put(cur.right)
