"""
1010.总持续时间可被 60 整除的歌曲

在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。
返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，我们希望下标数字 i 和 j 满足  i < j 且有 (time[i] + time[j]) % 60 == 0。

data: 2025-11-16
"""
from collections import defaultdict
from typing import List
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        ant = defaultdict(int)
        for t in time:
            ans += ant[(60 - t % 60) % 60]
            ant[t % 60] += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    time = [30,20,150,100,40]
    print(sol.numPairsDivisibleBy60(time))  # 3