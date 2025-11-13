"""
461.汉明距离

两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

data:2025-11-11

"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()

if __name__ == "__main__":
    sol = Solution()
    x = 1
    y = 4
    print(sol.hammingDistance(x, y))  # 2