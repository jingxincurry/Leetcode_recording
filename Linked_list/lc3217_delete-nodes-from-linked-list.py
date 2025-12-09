"""
3217.删除链表中的节点

给你一个链表的头节点 head 和一个整数 k 。删除链表的倒数第 k 个节点，并返回 头节点 。

data:2025-12-5
"""

from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        st = set(nums)
        while cur.next:
            if cur.next.val in st:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
if __name__ == "__main__":
    # 示例链表：1 -> 2 -> 3 -> 4 -> 5，nums = [2, 4]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    nums = [2, 4]
    sol = Solution()
    new_head = sol.modifiedList(nums, head)

    # 输出处理后的链表
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 1 -> 3 -> 5