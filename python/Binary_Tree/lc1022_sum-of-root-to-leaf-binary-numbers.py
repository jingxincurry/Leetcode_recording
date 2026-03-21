"""
1022. 从根到叶的二进制数之和
给出一棵二叉树，其上每个节点的值为 0 或 1 。每一条从根到叶子节点的路径都代表一个二进制数：
- 例如，从根到叶子节点的路径 0 -> 1 -> 1 表示二进制数 011 ，即十进制数 3 。
计算从根到叶子节点生成的所有二进制数之和。题目数据保证答案符合 32 位整数范围。

date: 2026-01-15
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], sum: int):
        if node is None:
            return 0
        sum = (sum << 1) | node.val
        if node.left is None and node.right is None:
            return sum
        return self.dfs(node.left, sum) + self.dfs(node.right, sum)
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     0   1
    #    / \ / \
    #   0  1 0  1
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)

    sol = Solution()
    total_sum = sol.sumRootToLeaf(root)
    print(f"从根到叶的二进制数之和: {total_sum}")  # 输出: 22