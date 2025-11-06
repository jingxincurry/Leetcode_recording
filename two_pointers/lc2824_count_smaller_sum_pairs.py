"""
2824.统计和小于目标的下标对数目

给你一个下标从 0 开始长度为 n 的整数数组 nums 和一个整数 target ，请你返回满足 0 <= i < j < n 且 nums[i] + nums[j] < target 的下标对 (i, j) 的数目。

data: 2025-11-6
"""
from typing import List
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums1 = [-1,1,2,3,1]
    target1 = 2
    print(sol.countPairs(nums1, target1))  # 3