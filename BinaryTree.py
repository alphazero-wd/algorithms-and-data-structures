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

class BST(BinaryTree):
  def __init__(self) -> None:
    super().__init__()
  
  def contains(self, val: int) -> bool:
    def find(root: Optional[TreeNode]):
      if not root: return False 
      if root.val == val: return True
      elif root.val > val: 
        return find(root.left)        
      else: return find(root.right)
    return find(self.root)
  
  def insert(self, val: int) -> None:
    new_node = TreeNode(val)
    if not self.root: 
      self.root = new_node
      return
    else:
      cur = self.root
      while True:
        if cur.val > val:
          if cur.left: cur = cur.left
          else: 
            cur.left = new_node
            break
        else:
          if cur.right: cur = cur.right
          else: 
            cur.right = new_node
            break
  
  def delete(self, val: int):
    def delete_recursively(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
      if not root: return
      if root.val > val:
        root.left = delete_recursively(root.left, val)
      elif root.val < val:
        root.right = delete_recursively(root.right, val)
      else:
        if not root.left and not root.right:
          return
        elif not root.left:
          root = root.right
          return root
        elif not root.right:
          root = root.left
          return root
        else:
          min_node: Optional[TreeNode] = self.find_min(root.right)
          root.val = min_node.val
          root.right = delete_recursively(root.right, min_node.val)
          return root
      return root
    return delete_recursively(self.root, val)

  def find_min(self) -> Optional[TreeNode]:
    cur = self.root                 
    while cur.left:
      cur = cur.left
    return cur
# BST Operations Time complexity
# h: height of the BST, n: # of nodes in the BST
# if the BST is balanced, h = log2(n)
# if the BST is unbalanced, h = n
# Operation           Analysis
# Find                O(h) 
# Insertion           O(h) 
# Deletion            O(h) 