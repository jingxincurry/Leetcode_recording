"""
2058.找到链表临界点之间的最小和最大距离
给你一个链表的头节点 head ，链表中每个节点都有一个 唯一的整数值 。
如果一个节点在链表中既不是第一个节点，也不是最后一个节点，并且它的值比它前面和后面的节点的值都要大或都要小，那么这个节点就是一个 临界点 。
注意，链表的头节点和尾节点 不能 是临界点。

data:2025-12-1
"""
from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        pre= head
        cur = head.next
        nxt = cur.next
        position = []
        index = 1

        while nxt:
            if (cur.val > pre.val and cur.val > nxt.val) or (cur.val < pre.val and cur.val < nxt.val):
                position.append(index)
            pre = cur
            cur = nxt
            nxt = nxt.next
            index += 1
        if len(position) < 2:
            return [-1, -1]

        minDistance = float('inf')
        for i in range(1, len(position)):
            minDistance = min(minDistance, position[i] - position[i - 1])
        maxDistance = position[-1] - position[0]
        return [minDistance, maxDistance]
if __name__ == "__main__":
    # 示例链表：1 -> 3 -> 2 -> 2 -> 3 -> 2 -> 2 -> 2 -> 7
    head = ListNode(1, ListNode(3, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(2, ListNode(2, ListNode(7)))))))))
    sol = Solution()
    print(sol.nodesBetweenCriticalPoints(head))  # 输出: [3, 3]