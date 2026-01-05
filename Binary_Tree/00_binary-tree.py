"""
145.二叉树的后序遍历

给你二叉树的根节点 root ，返回其节点值的 后序遍历 。

data:2026-01-04
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 前序遍历
    def preorder(self, root:TreeNode, res:List[int]):
        if root is None:
            return
        res.append(root.val)
        self.preorder(root.left,res)
        self.preorder(root.right,res)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.preorder(root, res)
        return res
    # 中序遍历
    def inorder(self, root:TreeNode, res:List[int]):
        if root is None:
            return
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res
    # 后序遍历
    def postorder(self, root:TreeNode, res:List[int]):
        if root is None:
            return
        self.postorder(root.left,res)
        self.postorder(root.right,res)
        res.append(root.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.postorder(root, res)
        return res
    
    

if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      /  \
    #     3    2
    #    / \   /
    #   4   6 3
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    sol = Solution()
    pre_result = sol.preorderTraversal(root)
    print(f"前序遍历结果: {pre_result}")  # 输出: 前序遍历结果: [1, 3, 4, 6, 2, 3]
    in_result = sol.inorderTraversal(root)
    print(f"中序遍历结果: {in_result}")  # 输出: 中序遍历结果: [4, 3, 6, 1, 3, 2]
    post_result = sol.postorderTraversal(root)
    print(f"后序遍历结果: {post_result}")  # 输出: 后序遍历结果: [3, 2, 1]