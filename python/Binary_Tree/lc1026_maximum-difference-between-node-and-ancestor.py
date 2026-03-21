"""
1026.节点与其祖先之间的最大差值

给定一个二叉树的根节点 root，找出该树中每个节点与其祖先节点之间的最大差值。
节点 A 是节点 B 的祖先节点，如果 A 在从根节点到 B 的路径上。

date: 2026-01-15
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], mn: int, mx: int):
        if node is None:
            return
        mn = min(mn, node.val)
        mx = max(mx, node.val)
        self.ans = max(self.ans, mx - node.val, node.val - mn)
        self.dfs(node.left, mn, mx)
        self.dfs(node.right, mn, mx)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
           self.ans = 0
           self.dfs(root, root.val, root.val)
           return self.ans
if __name__ == "__main__":
    # 构建示例二叉树
    #       8
    #      / \
    #     3   10
    #    / \    \
    #   1   6    14
    #      / \   /
    #     4   7 13
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    sol = Solution()
    max_diff = sol.maxAncestorDiff(root)
    print(f"节点与其祖先之间的最大差值: {max_diff}")  # 输出: 7