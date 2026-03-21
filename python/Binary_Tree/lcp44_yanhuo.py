"""
LCP 44. 开幕式焰火

计算巨型焰火中有多少种不同颜色的焰火。

date: 2026-01-27
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def dfs(self, node: TreeNode):
        if node is None:
            return 
        if node.val not in self.ant:
            self.ant.add(node.val)
            self.cnt += 1
        self.dfs(node.left)
        self.dfs(node.right)

    def numColor(self, root: TreeNode) -> int:
        self.cnt = 0
        self.ant = set()
        self.dfs(root)
        return self.cnt
if __name__ == "__main__":
    # 构建示例二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   2   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    sol = Solution()
    color_count = sol.numColor(root)
    print(f"不同颜色的焰火种类数: {color_count}")  # 输出: 4