"""
965.单值二叉树
如果一棵二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

date: 2026-01-22
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode]):
        if node is None:
            return True
        if node.val != self.ans:
            return False
        return self.dfs(node.left) and self.dfs(node.right)

    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.ans = root.val
        return self.dfs(root)
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     1   1
    #    / \
    #   1   1
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    sol = Solution()
    print(sol.isUnivalTree(root))  # 输出: True