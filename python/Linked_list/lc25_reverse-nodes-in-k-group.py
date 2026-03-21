"""
25.k个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 k 是一个正整数，它的值小于或等于链表的长度。

data:2025-12-25
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1
        
        dummy = ListNode(0)
        dummy.next = head
        p0 = dummy
        
        while n >= k:
            n -= k
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next
if __name__ == "__main__":
    # 创建示例链表: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    k = 2

    sol = Solution()
    modified_head = sol.reverseKGroup(head, k)

    # 输出处理后的链表
    current = modified_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 2 -> 1 -> 4 -> 3 -> 5