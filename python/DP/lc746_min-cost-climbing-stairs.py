"""
746.最小成本爬楼梯
数组的每个元素代表从该位置开始爬楼梯的成本，求最小的总成本。每次可以爬1或2个台阶，可以从第0或第1个台阶开始。

date: 2026-02-27
"""
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0] * (n + 1)
        for i in range(2, n + 1):
            f[i] = min(f[i -1] + cost[i - 1], f[i - 2] + cost[i - 2])
        return f[n]
if __name__ == "__main__":
    sol = Solution()
    print(sol.minCostClimbingStairs([10, 15, 20]))  # 输出: 15
    print(sol.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 输出: 6