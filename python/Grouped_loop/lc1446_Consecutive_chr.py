"""
1446.连续字符

给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。
请你返回字符串 s 的 能量。

data:2025-11-10
"""

class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 1
        cnt = 1
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
                max_len = max(cnt, max_len)
            else:
                cnt = 1
        return max_len
if __name__ == "__main__":
    sol = Solution()
    s = "leetcode"
    print(sol.maxPower(s))  # 2