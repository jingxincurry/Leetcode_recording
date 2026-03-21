"""
3643.垂直翻转子矩阵

给你一个 m x n 的整数矩阵 grid，以及三个整数 x、y 和 k。
整数 x 和 y 表示一个 正方形子矩阵 的左上角下标，整数 k 表示该正方形子矩阵的边长。
你的任务是垂直翻转子矩阵的行顺序。
返回更新后的矩阵。

Date: 2025-11-5
"""
from typing import List 
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l,r = x, x + k - 1
        while l < r:
            for j in range(y, y + k):
                grid[l][j], grid[r][j] = grid[r][j], grid[l][j]
            l += 1
            r -= 1
        return grid

if __name__ == "__main__":
    sol = Solution()
    grid1 = [[1,2,3],[4,5,6],[7,8,9]]
    x1, y1, k1 = 0, 0, 2
    print(sol.reverseSubmatrix(grid1, x1, y1, k1))  # [[4,2,3],[1,5,6],[7,8,9]]

    grid2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    x2, y2, k2 = 1, 1, 3
    print(sol.reverseSubmatrix(grid2, x2, y2, k2))  # [[1,2,3,4],[13,14,15,8],[9,10,11,12],[5,6,7,16]]