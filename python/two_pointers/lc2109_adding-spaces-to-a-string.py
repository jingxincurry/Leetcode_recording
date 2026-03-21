"""
2109.向字符串添加空格

给你一个下标从 0 开始的字符串 s ，以及一个下标从 0 开始的整数数组 spaces 。
数组 spaces 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 之前 。
例如，s = "EnjoyYourCoffee" 且 spaces = [5, 9] ，那么我们需要在 'Y' 和 'C' 之前添加空格，这两个字符分别位于下标 5 和下标 9 。因此，最终得到 "Enjoy Your Coffee" 。
请你添加空格，并返回修改后的字符串。

data:2025-11-14
"""
from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        j = 0
        for i,x in enumerate(s):
            if j < len(spaces) and i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(x)
        return "".join(ans)

if __name__ == "__main__":
    sol = Solution()
    s = "EnjoyYourCoffee"
    spaces = [5,9]
    print(sol.addSpaces(s, spaces))  # "Enjoy Your Coffee"