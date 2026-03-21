"""
817.链表组件

给定链表头结点 head，该链表上的每个结点都有一个 唯一的整型值 。同时给定列表 nums，该列表是上述链表中整型值的一个子集。
返回列表 nums 中组件的个数，这里对组件的定义为：链表中一段最长连续结点的值（该值必须在列表 nums 中）构成的集合。

data:2025-12-5
"""

from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        st = set(nums)
        ans = 0
        inset = False
        while head:
            if head.val not in st:
                inset = False
            elif not inset:
                inset = True
                ans += 1
            head = head.next
        return ans
if __name__ == "__main__":
    # 示例链表：0 -> 1 -> 2 -> 3，nums = [0, 1, 3]
    head = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
    nums = [0, 1, 3]
    sol = Solution()
    print(sol.numComponents(head, nums))  # 输出: 2