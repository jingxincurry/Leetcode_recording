"""
725.分隔链表
给定一个头结点为 head 的链表，以及一个整数 k，将链表分隔为 k 个连续的部分。
每部分的长度应该尽可能的相等：每两部分的长度差距不能超过 1 。这可能会导致某些部分为 null 。
返回一个符合上述规则的链表部分列表。

data:2025-12-5
"""
from typing import Optional
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cnt = []
        res,l = head, 0
        while res:
            res = res.next
            l += 1
        part_length = l // k
        remain = l % k
        cur = head
        for i in range(k):
            part_head = cur
            cur_part_length = part_length
            if remain:
                cur_part_length += 1
                remain -= 1
            for j in range(cur_part_length-1):
                if cur:
                    cur = cur.next
            # 后续还有节点，断开
            if cur:
                next_part = cur.next
                cur.next = None
                cur = next_part
            cnt.append(part_head)
        return cnt
if __name__ == "__main__":
    # 示例链表：1 -> 2 -> 3 -> 4 -> 5，k = 3
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 3
    sol = Solution()
    parts = sol.splitListToParts(head, k)
    
    # 输出分隔后的链表部分
    for i, part in enumerate(parts):
        print(f"Part {i + 1}: ", end="")
        current = part
        while current:
            print(current.val, end=" -> " if current.next else "")
            current = current.next
        if not part:
            print("None")
    # 输出:
    # Part 1: 1 -> 2
    # Part 2: 3 -> 4
    # Part 3: 5