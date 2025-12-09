"""
83.删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。返回已排序的链表。

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
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
if __name__ == "__main__":
    # 示例链表：1 -> 1 -> 2 -> 3 -> 3
    head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
    sol = Solution()
    new_head = sol.deleteDuplicates(head)

    # 输出处理后的链表
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 1 -> 2 -> 3