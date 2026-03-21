"""
1470.重新排列数组

给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。
请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

date: 2025-11-15
"""
from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [0] * (2 * n)
        for i in range(2 * n):
            if i % 2 == 0:
                ans[i] = nums[i // 2]
            else:
                ans[i] = nums[n + i // 2]
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums = [2,5,1,3,4,7]
    n = 3
    print(sol.shuffle(nums, n))  # [2,3,5,4,1,7]