"""
2348.全0子数组的数目

给你一个整数数组 nums ，返回全部为 0 的 子数组 数目。
子数组 是一个数组中一段连续非空元素组成的序列。

data:2025-11-10
"""
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        last = -1
        for i, x in enumerate(nums):
            if x:
                last = i
            else:
                ans += i - last
        return ans
    
if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,0,2,0,0]
    print(sol.zeroFilledSubarray(nums))  # 9