"""
1512.好数对的数目

给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。

data: 2025-11-16
"""
from typing import List
from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        ant = defaultdict(int)
        for i, x in enumerate(nums):
            ans += ant[x]
            ant[x] += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,1,1,3]
    print(sol.numIdenticalPairs(nums))  # 4