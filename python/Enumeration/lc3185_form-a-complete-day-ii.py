"""
3185.构成整天的下标对数目 II

给你一个整数数组 hours，表示以 小时 为单位的时间，返回一个整数，表示满足 i < j 且 hours[i] + hours[j] 构成 整天 的下标对 i, j 的数目。
整天 定义为时间持续时间是 24 小时的 整数倍 。
例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。

date: 2025-11-16

与1010.总持续时间可被 60 整除的歌曲对数目 方法一样
"""
from typing import List
from collections import defaultdict
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        ant = defaultdict(int)
        for h in hours:
            ans += ant[(24 - h % 24) % 24]
            ant[h % 24] += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    hours = [12,36,24,48,60]
    print(sol.countCompleteDayPairs(hours))  # 4