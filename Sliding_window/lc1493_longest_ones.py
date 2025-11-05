"""
1493.删掉一个元素以后全为1的最长子数组
给你一个二进制数组 nums ，你需要从中删掉一个元素。
请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。
如果不存在这样的子数组，请返回 0 。

Date: 2025-11-4
"""
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        ans = 0
        cnt0 = 0
        for right, x in enumerate(nums):
            cnt0 += 1 - x
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 1, 0, 1]
    print(sol.longestSubarray(nums1))