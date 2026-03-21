"""
129. 求根节点到叶节点数字之和

给你一个二叉树的根节点 root ，每个节点都包含一个 0-9 的数字。 每条从根节点到叶节点的路径都代表一个数字：
- 例如，从根节点到叶节点的路径 1 -> 2 -> 3 代表数字 123 。
计算从根节点到叶节点生成的所有数字之和。
返回这些数字之和 。

date: 2026-01-12
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node:Optional[TreeNode], sum: int):
        if node is None:
            return 0
        sum = sum*10 + node.val
        if node.left is None and node.right is None:
            return sum
        return self.dfs(node.left, sum) + self.dfs(node.right, sum)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    total_sum = sol.sumNumbers(root)
    print(f"从根节点到叶节点生成的所有数字之和: {total_sum}")  # 输出: 25