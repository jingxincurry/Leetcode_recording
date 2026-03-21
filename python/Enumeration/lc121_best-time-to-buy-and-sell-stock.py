"""
121.买卖股票的最佳时机

给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

date: 2025-11-15
"""
from typing import List
from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = inf
        p = 0
        pm = 0
        for x in prices:
            buy = min(buy, x)
            p = x - buy
            pm = max(pm, p)
        return pm
if __name__ == "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))  # 5