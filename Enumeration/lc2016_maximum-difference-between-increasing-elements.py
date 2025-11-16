"""
2016.增量元素之间的最大差值

给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] 。
返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。

date: 2025-11-16

知识点
if ans:
    return ans
else:
    return -1
可以写成  return ans or -1

"""
from typing import List
from math import inf
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        p = nums[0]       
        mx = -1
        for i in range(1, len(nums)):
            ans = nums[i] - p
            if ans > 0:
                mx = max(mx, ans)
            p = min(p, nums[i])
        return mx
if __name__ == "__main__":
    sol = Solution()
    nums = [9,4,3,2]
    print(sol.maximumDifference(nums))  # 4