"""
2657.找到两个数组的前缀公共数组

给你两个下标从 0 开始长度为 n 的整数排列 A 和 B 。
A 和 B 的 前缀公共数组 定义为数组 C ，其中 C[i] 是数组 A 和 B 到下标为 i 之前公共元素的数目。
请你返回 A 和 B 的 前缀公共数组 。
如果一个长度为 n 的数组包含 1 到 n 的元素恰好一次，我们称这个数组是一个长度为 n 的 排列 。

data:2025-11-13
"""
from typing import List
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans = []
        p, q = 0, 0
        for x, y in zip(A, B):
            p |= 1 << x
            q |= 1 << y
            ans.append((p & q).bit_count())
        return ans
if __name__ == "__main__":
    sol = Solution()
    A = [1,3,2,4]
    B = [3,1,2,4]
    print(sol.findThePrefixCommonArray(A, B))  # [0,1,2,3,5]