"""
111.二叉树的最小深度
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。
示例 1:
输入: root = [3,9,20,null,null,15,7]
输出: 2

date: 2026-01-07
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode]):
        if not node.left and not node.right:
            return 1
        if not node.left:
            return 1 + self.dfs(node.right)
        if not node.right:
            return 1 + self.dfs(node.left)
        return 1 + min(self.dfs(node.left), self.dfs(node.right))
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root)
if __name__ == "__main__":
    # 构建示例二叉树
    #       3
    #      / \
    #     9  20
    #        / \
    #       15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    depth = sol.minDepth(root)
    print(f"最小深度: {depth}")  # 输出: 最小深度: 2