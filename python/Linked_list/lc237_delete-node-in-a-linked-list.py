"""
237.删除链表中的节点

请编写一个函数来删除单链表中的某个节点。你将被给定要删除的节点的引用。你不需要访问头节点。
现有一个链表 -- head = [4,5,1,9]，它可以表示为:
    4 -> 5 -> 1 -> 9
示例 1: 
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
if __name__ == "__main__":
    # 创建示例链表 4 -> 5 -> 1 -> 9
    head = ListNode(4)
    node_to_delete = ListNode(5)
    head.next = node_to_delete
    node_to_delete.next = ListNode(1)
    node_to_delete.next.next = ListNode(9)

    sol = Solution()
    sol.deleteNode(node_to_delete)

    # 输出处理后的链表
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # 输出: 4 -> 1 -> 9