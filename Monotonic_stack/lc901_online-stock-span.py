"""
901.股票价格跨度

设计一个算法收集某些股票的每日报价，并返回该股票当日价格的 跨度 。

当日股票价格的 跨度 被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来 7 天股票的价格是 [100,80,60,70,60,75,85]，那么股票跨度将是 [1,1,1,2,1,4,6] 。
实现 StockSpanner 类：
StockSpanner() 初始化类对象。
int next(int price) 给出今天的股价 price ，返回该股票当日价格的 跨度 。

data: 2025-11-21

有点困难：结构
"""
from typing import List

class StockSpanner:
    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1
        while self.st and price >= self.st[-1][0]:
            span += self.st.pop()[1]
        self.st.append((price, span))
        return span
if __name__ == "__main__":
    sol = StockSpanner()
    # ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    # [[], [100], [80], [60], [70], [60], [75], [85]]
    print(sol.next(100))  # 1
    print(sol.next(80))   # 1
    print(sol.next(60))   # 1
    print(sol.next(70))   # 2
    print(sol.next(60))   # 1
    print(sol.next(75))   # 4
    print(sol.next(85))   # 6