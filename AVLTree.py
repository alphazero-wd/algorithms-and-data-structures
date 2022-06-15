from typing import Optional


class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class AVLTree:
    def insert(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        elif root.val > val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        balance_factor = self.get_balance_factor(root)

        # left left rotation
        if balance_factor > 1 and val < root.left.val:
            return self.rotate_right(root)

        # right right rotation
        if balance_factor < -1 and val > root.right.val:
            return self.rotate_left(root)

        # left right rotation
        if balance_factor > 1 and val > root.left.val:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # right left rotation
        if balance_factor < -1 and val < root.right.val:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def rotate_left(self, z: Optional[TreeNode]) -> Optional[TreeNode]:
        y = z.right
        temp = y.left

        y.left = z
        z.right = temp
        return y

    def rotate_right(self, z: Optional[TreeNode]) -> Optional[TreeNode]:
        y = z.left
        temp = y.right

        y.right = z
        z.left = temp
        return y

    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def get_balance_factor(self, root: Optional[TreeNode]) -> int:
        return self.get_height(root.left) - self.get_height(root.right)

    def preorder(self, root: Optional[TreeNode]):
        if not root:
            return
        print("{0} ".format(root.val), end="")
        self.preorder(root.left)
        self.preorder(root.right)
