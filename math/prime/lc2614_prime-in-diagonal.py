"""
2614.对角线上的质数最大值

给你一个下标从 0 开始的二维整数数组 nums 。

返回位于 nums 至少一条 对角线 上的最大 质数 。如果任一对角线上均不存在质数，返回 0 。
注意：
如果某个整数大于 1 ，且不存在除 1 和自身之外的正整数因子，则认为该整数是一个质数。
如果存在整数 i ，使得 nums[i][i] = val 或者 nums[i][nums.length - i - 1]= val ，则认为整数 val 位于 nums 的一条对角线上。

date: 2025-11-18
"""
from typing import List
from math import isqrt
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        m = 0
        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x >= 2
        
        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                m = max(m, nums[i][i])
            if is_prime(nums[i][len(nums) - i - 1]):
                m = max(m, nums[i][len(nums) - i - 1])
        return m
if __name__ == "__main__":
    sol = Solution()
    nums = [[1,2,3],[5,6,7],[9,10,11]]
    print(sol.diagonalPrime(nums))  # 11