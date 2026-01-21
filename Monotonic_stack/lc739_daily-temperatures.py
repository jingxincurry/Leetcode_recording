"""
739.每日温度

给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

data:2025-11-21
"""
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        right = [0] * n
        st = []
        for i in range(n -1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                right[i] = st[-1] - i
            st.append(i)
        return right
if __name__ == "__main__":
    solu = Solution()
    temperatures = [73,74,75,71,69,72,76,73]
    print(solu.dailyTemperatures(temperatures))  # 输出[1,1,4,2,1,1,0,0]