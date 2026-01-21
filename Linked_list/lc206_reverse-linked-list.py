"""
206.反转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

data:2025-12-25
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
if __name__ == "__main__":
    # 创建示例链表: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    # 输出反转后的链表
    current = reversed_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 5 -> 4 -> 3 -> 2 -> 1