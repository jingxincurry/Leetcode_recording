"""
1290.二进制链表转整数
给你一个单链表的头节点 head ，该链表表示一个非负的二进制数。
请你返回该链表所表示数字的十进制值。


"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ans = 0
        while head:
            ans = ans * 2 + head.val
            head = head.next
        return ans
if __name__ == "__main__":
    # 示例：链表 1 -> 0 -> 1 表示二进制数 101，十进制值为 5
    head = ListNode(1, ListNode(0, ListNode(1)))
    sol = Solution()
    print(sol.getDecimalValue(head))  # 输出: 5
    