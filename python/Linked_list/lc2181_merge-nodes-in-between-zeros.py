# Definition for singly-linked list.
"""
2181.在零之间合并节点
给你一个链表的头节点 head ，该链表包含若干节点。节点的值不是 0 就是 1 。链表以 0 开头和结尾，并且在两个 0 之间总是有若干 1 。
你的任务是：合并每两个 0 之间的所有节点，将它们的和作为一个新节点，最后返回一个修改后链表的头节点，该链表不包含任何 0 。

data:2025-12-5

"""
from typing import Optional
from typing import List 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        head = head.next

        ans = 0
        while head:
            if head.val != 0:
                ans += head.val        
            else:
                cur.next = ListNode(ans)
                ans = 0
                cur = cur.next
            head = head.next
        return dummy.next
if __name__ == "__main__":
    # 示例链表：0 -> 1 -> 0 -> 3 -> 0 -> 2 -> 2 -> 0
    head = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
    sol = Solution()
    new_head = sol.mergeNodes(head)

    # 输出处理后的链表
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 1 -> 3 -> 4
            