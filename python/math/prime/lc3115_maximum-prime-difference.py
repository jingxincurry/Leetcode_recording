"""
3115.质数的最大距离

给你一个整数数组 nums。
返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。

data:2025-11-17

"""
from typing import List
from math import isqrt
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x >= 2
        left = -1
        right = -1
        for i in range(len(nums)):
            if is_prime(nums[i]):
                if left == -1:
                    left = i
                right = i
        return right - left
if __name__ == "__main__":
    sol = Solution()
    nums = [4,6,8,10]
    print(sol.maximumPrimeDifference(nums))  # -1