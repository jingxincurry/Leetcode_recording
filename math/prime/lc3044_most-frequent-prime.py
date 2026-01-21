"""
3044.出现频率最高的质数

给你一个大小为 m x n 、下标从 0 开始的二维矩阵 mat 。在每个单元格，你可以按以下方式生成数字：

最多有 8 条路径可以选择：东，东南，南，西南，西，西北，北，东北。
选择其中一条路径，沿着这个方向移动，并且将路径上的数字添加到正在形成的数字后面。
注意，每一步都会生成数字，例如，如果路径上的数字是 1, 9, 1，那么在这个方向上会生成三个数字：1, 19, 191 。
返回在遍历矩阵所创建的所有数字中，出现频率最高的、大于 10的质数；如果不存在这样的质数，则返回 -1 。如果存在多个出现频率最高的质数，那么返回其中最大的那个。
注意：移动过程中不允许改变方向。

data:2025-11-18
"""
from typing import List
from collections import defaultdict
from math import isqrt
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        def is_prime(n: int) -> bool:
            for i in range(2, isqrt(n) + 1):
                if n % i == 0:
                    return False
            return n >= 2  # 1 不是质数
        cnt = defaultdict(int)
        dics = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        for i in range(m):
            for j in range(n):
                for dx, dy in dics:
                    ii, jj = i + dx, j + dy
                    val = mat[i][j]
                    while 0 <= ii < m and 0 <= jj < n:
                        val = val * 10 + mat[ii][jj]
                        if is_prime(val):
                            cnt[val] += 1
                        ii += dx
                        jj += dy
        if not cnt:
            return -1 
        ans, max_cnt = -1, 0
        for num, freq in cnt.items(): # 键，值
            if freq > max_cnt:
                ans, max_cnt = num, freq
            elif freq == max_cnt:
                ans = max(ans, num)
        return ans
if __name__ == "__main__":
    sol = Solution()
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    print(sol.mostFrequentPrime(mat))  # -1