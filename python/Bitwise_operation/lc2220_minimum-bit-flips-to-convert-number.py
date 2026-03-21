"""
2220.转换数字的最少位翻转次数

一次 位翻转 定义为将数字 x 二进制中的一个位进行 翻转 操作，即将 0 变成 1 ，或者将 1 变成 0 。
比方说，x = 7 ，二进制表示为 111 ，我们可以选择任意一个位（包含没有显示的前导 0 ）并进行翻转。比方说我们可以翻转最右边一位得到 110 ，或者翻转右边起第二位得到 101 ，或者翻转右边起第五位（这一位是前导 0 ）得到 10111 等等。
给你两个整数 start 和 goal ，请你返回将 start 转变成 goal 的 最少位翻转 次数。

data:2025-11-11

知识点：异或 + bit_count()
"""

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start ^ goal).bit_count()
    
if __name__ == "__main__":
    sol = Solution()
    start = 10
    goal = 7
    print(sol.minBitFlips(start, goal))  # 3