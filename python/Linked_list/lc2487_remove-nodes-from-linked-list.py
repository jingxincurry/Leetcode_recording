"""
2487.从链表中移除节点
给你一个链表的头节点 head ，请你删除链表中所有满足以下条件的节点。
返回修改后链表的头节点 head 。

data:2025-12-25
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return head
        node = self.removeNodes(head.next)
        if node.val > head.val:
            return node
        head.next = node
        return head
if __name__ == "__main__":
    # 创建示例链表: 5 -> 2 -> 13 -> 3 -> 8
    head = ListNode(5)
    head.next = ListNode(2)
    head.next.next = ListNode(13)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(8)

    sol = Solution()
    modified_head = sol.removeNodes(head)

    # 输出处理后的链表
    current = modified_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 13 -> 8