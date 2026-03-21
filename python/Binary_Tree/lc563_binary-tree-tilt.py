"""
563. 二叉树的坡度

给定一个二叉树，计算 整个树 的坡度 。 一个树的 坡度 定义为：每个节点的坡度之和。 每个节点的 坡度 定义为：该节点左子树的节点值之和
减去右子树节点值之和的绝对值。 如果没有左子树的话，左子树节点值之和为 0 ； 如果没有右子树的话，右子树节点值之和为 0 。 空节点的坡度是 0 。
返回整个树的坡度 。

date: 2026-01-27
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
        sum_left = self.dfs(node.left)
        sum_right = self.dfs(node.right)
        self.ans += abs(sum_left - sum_right)
        return sum_left + sum_right + node.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     2   3
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    sol = Solution()
    tilt = sol.findTilt(root)
    print(f"二叉树的坡度: {tilt}")  # 输出: 1