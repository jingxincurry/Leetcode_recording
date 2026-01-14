"""
116.填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}  
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

date: 2026-01-06
"""
from typing import List
from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def dfs(self, node: 'Optional[Node]', depth: int, res: 'List[Node]'):
        if node is None:
            return 
        if depth == len(res):
            res.append(node)
        else:
            res[depth].next = node
            res[depth] = node
        self.dfs(node.left, depth + 1, res)
        self.dfs(node.right, depth + 1, res)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        self.dfs(root, 0, res)
        return root
if __name__ == "__main__":
    # 构建示例完美二叉树
    #        1
    #      /   \
    #     2     3
    #    / \   / \
    #   4   5 6   7
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    sol = Solution()
    connected_root = sol.connect(root)

    # 输出每个节点的 next 指针值
    level_start = connected_root
    while level_start:
        current = level_start
        level_start = None
        next_level_first_node = None
        while current:
            next_val = current.next.val if current.next else None
            print(f"Node {current.val} -> Next {next_val}")
            if not level_start:
                if current.left:
                    level_start = current.left
                elif current.right:
                    level_start = current.right
            current = current.next
        print("-----")