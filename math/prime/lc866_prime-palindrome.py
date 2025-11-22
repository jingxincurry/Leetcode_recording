"""
866.回文素数

给你一个整数 n ，返回大于或等于 n 的最小 回文质数。
一个整数如果恰好有两个除数：1 和它本身，那么它是 质数 。注意，1 不是质数。
例如，2、3、5、7、11 和 13 都是质数。
一个整数如果从左向右读和从右向左读是相同的，那么它是 回文数 。

例如，101 和 12321 都是回文数。
测试用例保证答案总是存在，并且在 [2, 2 * 108] 范围内。

data: 2025-11-19
"""
from math import isqrt
class Solution:
    def is_prime(self, n: int) -> bool:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return n >= 2  # 1 不是质数


    def reverse(self, x: int) -> int:
        ans = 0
        while x:
            ans = 10* ans + x % 10
            x //= 10
        return ans


    def primePalindrome(self, n: int) -> int:
        while True:
            if n == self.reverse(n) and self.is_prime(n):
                return n
            n += 1
            if 10**7 < n < 10**8:
                n = 10**8
if __name__ == "__main__":
    sol = Solution()
    n = 31
    print(sol.primePalindrome(n))  # 101