"""
988. 从叶结点开始的最小字符串

给定一颗根结点为 root 的二叉树，树中的每一个结点都有一个 [0, 25] 范围内的值，分别代表字母 'a' 到 'z'。
返回 按字典序最小 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束。
注：字符串中任何较短的前缀在 字典序上 都是 较小 的：
例如，在字典序上 "ab" 比 "aba" 要小。叶结点是指没有子结点的结点。 
节点的叶节点是没有子节点的节点。

date: 2026-01-13
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], path:str):
        if node is None:
            return 
        path = chr(ord('a') + node.val) + path
        if node.left is None and node.right is None:
            if self.ans is None or path < self.ans:
                self.ans = path
        self.dfs(node.left, path)
        self.dfs(node.right, path)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = None
        self.dfs(root, "")
        return self.ans
if __name__ == "__main__":
    # 构建示例二叉树
    #       0
    #      / \
    #     1   2
    #    / \  / \
    #   3  4 3   4
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)

    sol = Solution()
    smallest_string = sol.smallestFromLeaf(root)
    print(f"从叶结点开始的最小字符串: {smallest_string}")  # 输出: "dba"