from typing import Optional
from queue import Queue


class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTree(object):
    def inorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end=' ')
        self.inorder(root.right)

    def preorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        print(root.val, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root: Optional[TreeNode]) -> None:
        if not root:
            return ''
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end=' ')

    def level_order(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        queue: Queue[TreeNode] = Queue()
        queue.put(root)
        while not queue.empty():
            cur = queue.get()
            print(cur.val, end=" ")
            if cur.left:
                queue.put(cur.left)
            if cur.right:
                queue.put(cur.right)
