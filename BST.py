from typing import Optional
from BinaryTree import BinaryTree, TreeNode


class BST(BinaryTree):
    def contains(self, root: Optional[TreeNode], val: int) -> bool:
        if not root:
            return
        if root.val == val:
            return root
        elif root.val > val:
            return self.contains(root.left, val)
        else:
            return self.contains(root.right, val)

    def insert(self, root: Optional[TreeNode], val: int) -> None:
        if not root:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)
        return root

    def delete(self, root: Optional[TreeNode], val: int):
        if not root:
            return
        if root.val > val:
            root.left = self.delete(root.left, val)
        elif root.val < val:
            root.right = self.delete(root.right, val)
        else:
            # case 1: delete a leaf node
            if not root.left and not root.right:
                root = None
            # case 2: node only has right child
            elif not root.left:
                root = root.right
            # case 3: node only has left child
            elif not root.right:
                root = root.left
            # case 4: node has both left and right children
            else:
                min_node = self.find_min(root.right)
                root.val = min_node.val
                root.right = self.delete(root.right, min_node.val)
            return root
        return root

    def find_min(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        while cur.left:
            cur = cur.left
        return cur
