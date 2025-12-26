"""
1669.合并两个链表

给你两个链表 list1 和 list2 ，它们包含的元素分别为 n 个和 m 个。
请你将 list1 中第 a 个节点到第 b 个节点（包含 a 和 b）删除，并将 list2 接在被删除节点的位置。

date: 2025-12-11
"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        preA = list1
        left = 0
        while left < a - 1:
            preA = preA.next
            left += 1
        
        afterB = preA
        while left <= b:
            afterB = afterB.next
            left += 1
        preA.next = list2

        tail = list2
        while tail.next:
            tail = tail.next
        tail.next = afterB
        return list1

if __name__ == "__main__":
    # 创建示例链表 list1: 0 -> 1 -> 2 -> 3 -> 4 -> 5
    list1 = ListNode(0)
    current = list1
    for i in range(1, 6):
        current.next = ListNode(i)
        current = current.next

    # 创建示例链表 list2: 1000000 -> 1000001 -> 1000002
    list2 = ListNode(1000000)
    current = list2
    for i in range(1000001, 1000003):
        current.next = ListNode(i)
        current = current.next

    a, b = 3, 4

    sol = Solution()
    merged_list = sol.mergeInBetween(list1, a, b, list2)

    # 输出处理后的链表
    current = merged_list
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 0 -> 1 -> 2 -> 1000000 -> 1000001 -> 1000002 -> 5