"""
611.有效三角形的个数

给定一个包含非负整数的数组 nums ，返回其中可以组成三角形三条边的三元组个数。

data:2025-11-9
"""
from typing import List
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += j - i
                    j -= 1
                else:
                    i += 1
        return count
if __name__ == "__main__":
    sol = Solution()
    nums = [2,2,3,4]
    print(sol.triangleNumber(nums))  # 3