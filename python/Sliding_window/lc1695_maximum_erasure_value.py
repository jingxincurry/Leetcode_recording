"""
1695.删除子数组的最大得分

给你一个正整数数组 nums ，请你从中删除一个含有 若干不同元素 的子数组。删除子数组的 得分 就是子数组各元素之 和 。
返回 只删除一个 子数组可获得的 最大得分 。
如果数组 b 是数组 a 的一个连续子序列，即如果它等于 a[l],a[l+1],...,a[r] ，那么它就是 a 的一个子数组。

Date: 2025-11-4
"""
from typing import List
from collections import defaultdict
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        left = 0
        s = 0
        ans = 0
        for right, x in enumerate(nums):
            dic[x] += 1
            s += x
            while dic[x] > 1:
                s -= nums[left]
                dic[nums[left]] -= 1
                left += 1
            ans = max(ans, s)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,2,4,5,6]
    print(sol.maximumUniqueSubarray(nums1))