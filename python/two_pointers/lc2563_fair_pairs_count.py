"""
2563.统计公平数对的数目

给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。
如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：
0 <= i < j < n，且
lower <= nums[i] + nums[j] <= upper

data: 2025-11-6
"""
from typing import List
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count(upper: int) ->int:
            left, right = 0, len(nums) - 1
            res = 0
            while left < right:
                s = nums[left] + nums[right]
                if s <= upper:
                    res += right - left
                    left += 1
                else:
                    right -= 1
            return res
        return count(upper) - count(lower - 1)
    
if __name__ == "__main__":
    sol = Solution()
    nums1 = [0,1,7,4,4,5]
    lower1 = 3
    upper1 = 6
    print(sol.countFairPairs(nums1, lower1, upper1))  # 6

    