"""
199.二叉树的右视图
给定一个二叉树的根节点 root，想象自己站在它的右侧，按从顶部到底部的顺序，返回从右侧所能看到的节点值。

data:2026-01-05
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node:Optional[TreeNode], depth: int, res: List[int]):
        if node is None:
            return
        if depth == len(res):
            res.append(node.val)
        self.dfs(node.right, depth + 1, res)
        self.dfs(node.left, depth + 1, res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, 0, res)
        return res
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     2   3
    #      \   \
    #       5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sol = Solution()
    result = sol.rightSideView(root)
    print(f"右视图结果: {result}")  # 输出: 右视图结果: [1, 3, 4]
