"""
1372. 二叉树中的最长交错路径
给你一棵以 root 为根的二叉树，找出最长的 交错路径 的长度。 交错路径 定义如下：
- 选择二叉树中 任意 节点和一个方向（左或者右）。
- 如果前进方向为左，那么移动到当前节点的左子节点，否则移动到右子节点。
- 改变前进方向：左变右或者右变左。  
- 重复第二步和第三步，直到你无法继续移动。
返回 交错路径 的最长长度。

date: 2026-01-17
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], l: int, r: int):

        self.ans = max(self.ans, l, r)
        if node.left:
            self.dfs(node.left, r + 1, 0)
        if node.right:
            self.dfs(node.right, 0, l + 1)

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0, 0)
        return self.ans
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #        \
    #         2
    #        /
    #       3
    #        \
    #         4
    #        /
    #       5
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.left.right = TreeNode(4)
    root.right.left.right.left = TreeNode(5)

    sol = Solution()
    longest_path = sol.longestZigZag(root)
    print(f"二叉树中的最长交错路径长度: {longest_path}")  # 输出: 4