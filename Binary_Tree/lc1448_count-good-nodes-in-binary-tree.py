"""
1448.统计二叉树中好节点的数目

给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
一个节点 X 被认为是好节点，当且仅当从根节点到该节点 X 的路径上不存在值大于 X 的节点。

date: 2026-01-12
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], mx: int):
        if node is None:
            return 0
        good = 1 if node.val >= mx else 0
        mx = max(mx, node.val)
        
        return good + self.dfs(node.left, mx) + self.dfs(node.right, mx)
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.dfs(root, root.val)
if __name__ == "__main__":
    # 构建示例二叉树
    #       3
    #      / \
    #     1   4
    #    /     \
    #   3       5
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(5)

    sol = Solution()
    good_node_count = sol.goodNodes(root)
    print(f"二叉树中好节点的数目: {good_node_count}")  # 输出: 4