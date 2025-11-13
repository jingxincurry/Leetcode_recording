"""
3370.仅含置位位的最小整数

给你一个正整数 n。
返回 大于等于 n 且二进制表示仅包含 置位 位的 最小 整数 x 。
置位 位指的是二进制表示中值为 1 的位。

data:2025-11-10
"""
class Solution:
    def smallestNumber(self, n: int) -> int:
        return (1 << n.bit_length()) - 1

if __name__ == "__main__":
    sol = Solution()
    n = 5
    print(sol.smallestNumber(n))  # 7