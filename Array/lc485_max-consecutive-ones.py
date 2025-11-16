"""
485.最大连续1的个数

给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。
"""
from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        res = 0
        for i, x in enumerate(nums):
            if x == 1:
                res += 1
                ans = max(ans, res)
            else:
                res = 0
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,0,1,1,1]
    print(sol.findMaxConsecutiveOnes(nums))  # 3