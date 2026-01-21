"""
24.两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换

data:2025-12-26
要点：
node0.next = node2
node2.next = node1
node1.next = node3
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node0 = dummy = ListNode(0)
        dummy.next = head
        node1 = head
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node0.next = node2
            node2.next = node1
            node1.next = node3

            node0 = node1
            node1 = node3
        return dummy.next
if __name__ == "__main__":
    # 创建示例链表: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    modified_head = sol.swapPairs(head)

    # 输出处理后的链表
    current = modified_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 2 -> 1 -> 4 -> 3