"""
623. 在二叉树中增加一行
给定一个二叉树的根节点 root 和两个整数 val 和 depth，在给定的深度 depth 处添加一行节点值为 val 的节点。
添加规则如下:
- 如果 depth == 1 意味着在树的最前面添加一个新根节点，新的根节点的值为 val，原来的树作为新根节点的左子树。
- 如果 depth > 1，遍历到深度为 depth - 1 的每个非空节点 cur，创建两个值为 val 的新节点作为 cur 的左子节点和右子节点。
  cur 原来的左子节点变成新左子节点的左子节点，cur 原来的右子节点变成新右子节点的右子节点。

date: 2026-01-17  
"""
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root == None:
            return
        if depth == 1:
            return TreeNode(val, root, None)
        if depth == 2:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth-1)
        return root
if __name__ == "__main__":
    # 构建示例二叉树
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   3  1 5  7
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)

    val = 1
    depth = 2

    sol = Solution()
    new_root = sol.addOneRow(root, val, depth)

    # 输出修改后的二叉树的根节点值以验证结果
    print(f"新根节点值: {new_root.val}")  # 输出: 新根节点值: 4
    print(f"左子节点值: {new_root.left.val}")  # 输出: 左子节点值: 1
    print(f"右子节点值: {new_root.right.val}")  # 输出: 右子节点值: 1