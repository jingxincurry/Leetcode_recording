"""
404.左叶子之和
计算给定二叉树的所有左叶子之和。

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
        if node is None:
            return 0
        ans = 0
        if node.left and not node.left.left and not node.left.right:
            ans += node.left.val
        ans += self.dfs(node.left)
        ans += self.dfs(node.right)
        return ans

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
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
    result = sol.sumOfLeftLeaves(root)
    print(f"左叶子之和: {result}")  # 输出: 左叶子之和: 24