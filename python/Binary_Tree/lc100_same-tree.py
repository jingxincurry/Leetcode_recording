"""
100.相同的树
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

date: 2026-01-22
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
if __name__ == "__main__":
    # 构建示例二叉树 p 和 q
    # 树 p:
    #        1
    #      /   \
    #     2     3
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # 树 q:
    #        1
    #      /   \
    #     2     3
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    sol = Solution()
    print(sol.isSameTree(p, q))  # 输出: True
        