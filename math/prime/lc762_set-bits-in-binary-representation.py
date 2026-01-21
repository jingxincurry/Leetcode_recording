"""
762.二进制表示中质数个计算置位

给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

计算置位位数 就是二进制表示中 1 的个数。

例如， 21 的二进制表示 10101 有 3 个计算置位。

data:2025-11-18
"""
from math import isqrt
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x >= 2
        for i in range(left, right + 1):
            if is_prime(i.bit_count()):
                ans += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    left = 6
    right = 10
    print(sol.countPrimeSetBits(left, right))  # 4