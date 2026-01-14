"""
872.叶子相似的树
请考虑一棵二叉树上所有的叶子节点。叶子节点是指没有子节点的节点。
如果两个二叉树的叶子节点值序列相同，则认为这两棵树是叶子相似的。
当且仅当两个二叉树的叶子节点值序列相同，我们才返回 true。

date: 2026-01-07
"""
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: Optional[TreeNode], ans:List[int]):
        if node is None:
            return
        if node.left is None and node.right is None:
            ans.append(node.val)
        self.dfs(node.left, ans)
        self.dfs(node.right, ans)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 = []
        ans2 = []
        self.dfs(root1, ans1)
        self.dfs(root2, ans2)
        # if len(ans1) == len(ans2):
        #     for i in range(len(ans1)):
        #         if ans1[i] != ans2[i]:
        #             return False
        #     return True
        # else:
        #     return False
        return ans1 == ans2
if __name__ == "__main__":
    # 构建示例二叉树1
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   9
    #      / \
    #     7   4
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.right = TreeNode(9)

    # 构建示例二叉树2
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   7   4
    #            \
    #             9
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(9)

    sol = Solution()
    result = sol.leafSimilar(root1, root2)
    print(f"两棵树是否叶子相似: {result}")  # 输出: 两棵树是否叶子相似: True