"""
1315. 二叉树中所有奇数长度路径节点之和
给你一棵二叉树的根节点 root ，返回所有 奇数长度路径 节点值之和。
奇数长度路径 是指从根节点到叶节点的路径上节点数为 奇数 的路径。

date: 2026-01-12
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], father: Optional[int], grandfather: Optional[int]):
        if root is None:
            return 0
        total = 0
        if grandfather is not None and grandfather % 2 == 0:
            total += root.val
        total += self.dfs(root.left, root.val, father)
        total += self.dfs(root.right, root.val, father)
        return total


    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, None, None)
if __name__ == "__main__":
    # 构建示例二叉树
    #       6
    #      / \
    #     7   8
    #    / \ / \
    #   2  7 1  3
    #  /  / \    \
    # 9  1   4    5
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    sol = Solution()
    total_sum = sol.sumEvenGrandparent(root)
    print(f"所有奇数长度路径节点值之和: {total_sum}")  # 输出: 18