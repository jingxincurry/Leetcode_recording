"""
82.删除排序链表中的重复元素 II
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中没有重复出现的数字。返回已排序的链表。

data:2025-12-5
"""
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.val == cur.next.next.val:
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
if __name__ == "__main__":
    # 示例链表：1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5)))))))
    sol = Solution()
    new_head = sol.deleteDuplicates(head)

    # 输出处理后的链表
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 1 -> 2 -> 5