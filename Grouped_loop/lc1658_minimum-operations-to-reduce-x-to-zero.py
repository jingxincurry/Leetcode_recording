"""
1658.将 x 减到 0 的最小操作数

给你一个整数数组 nums 和一个整数 x 。每一次操作时，你应当移除数组 nums 最左边或最右边的元素，然后从 x 中减去该元素的值。请注意，需要 修改 数组以供接下来的操作使用。
如果可以将 x 恰好 减到 0 ，返回 最小操作数 ；否则，返回 -1 。

data:2025-11-19
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x
        if target < 0:
            return -1
        s = left = 0
        ans = -1 
        for right,x in enumerate(nums):
            s += x
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans

if __name__ == "__main__":  
    sol = Solution()
    nums = [1,1,4,2,3]
    x = 5
    print(sol.minOperations(nums, x))  # 2