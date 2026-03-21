"""
3456.找出长度为K 的特殊子字符串

给你一个字符串 s 和一个整数 k。

判断是否存在一个长度 恰好 为 k 的子字符串，该子字符串需要满足以下条件：

该子字符串 只包含一个唯一字符（例如，"aaa" 或 "bbb"）。
如果该子字符串的 前面 有字符，则该字符必须与子字符串中的字符不同。
如果该子字符串的 后面 有字符，则该字符也必须与子字符串中的字符不同。
如果存在这样的子串，返回 true；否则，返回 false。
子字符串 是字符串中的连续、非空字符序列。

date: 2025-11-10
"""

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        cnt = 0
        for i, x in enumerate(s):
            cnt += 1
            if i == len(s) - 1 or x != s[i + 1]:
                if cnt == k:
                    return True
                cnt = 0
        return False
if __name__ == "__main__":
    sol = Solution()
    s = "aaabbbcc"
    k = 3
    print(sol.hasSpecialSubstring(s, k))  # True