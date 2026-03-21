"""
2001.可互换矩形的组数

用一个下标从 0 开始的二维整数数组 rectangles 来表示 n 个矩形，其中 rectangles[i] = [widthi, heighti] 表示第 i 个矩形的宽度和高度。
如果两个矩形 i 和 j（i < j）的宽高比相同，则认为这两个矩形 可互换 。更规范的说法是，两个矩形满足 widthi/heighti == widthj/heightj（使用实数除法而非整数除法），则认为这两个矩形 可互换 。
计算并返回 rectangles 中有多少对 可互换 矩形。

date: 2025-11-16

myself-solutions
"""
from typing import List
from collections import defaultdict
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ant = defaultdict(int)
        ans = 0
        d = 0
        for i in range(len(rectangles)):
            ans = rectangles[i][0] / rectangles[i][1]
            d += ant[ans]
            ant[ans] += 1
        return d
if __name__ == "__main__":
    sol = Solution()
    rectangles = [[4,8],[3,6],[10,20],[15,30]]
    print(sol.interchangeableRectangles(rectangles))  # 6