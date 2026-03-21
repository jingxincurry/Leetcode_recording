"""
2030.移除链表元素

删除链表中等于给定值 val 的所有节点。

"""
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next  
        return dummy.next
if __name__ == "__main__":
    # 示例链表：1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6，val = 6
    head = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
    val = 6
    sol = Solution()
    new_head = sol.removeElements(head, val)

    # 输出处理后的链表
    current = new_head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 1 -> 2 -> 3 -> 4 -> 5