"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

data: 2026-02-27
"""
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.climbStairs(2))  # 输出: 2
    print(sol.climbStairs(3))  # 输出: 3