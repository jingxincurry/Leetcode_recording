"""
1356.根据数字二进制下1的数目排序

给你一个整数数组 arr 。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。
如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。
请你返回排序后的数组。

data:2025-11-11
"""
from typing import List
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x :(x.bit_count(), x))

if __name__ == "__main__":
    sol = Solution()
    arr = [0,1,2,3,4,5,6,7,8]
    print(sol.sortByBits(arr))  # [0,1,2,4,8,3,5,6,7]