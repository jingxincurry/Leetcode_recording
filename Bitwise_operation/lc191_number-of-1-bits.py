"""
191.位1的个数

给定一个正整数 n，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。

data:2025-11-13
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
if __name__ == "__main__":
    sol = Solution()
    n = 11
    print(sol.hammingWeight(n))  # 3