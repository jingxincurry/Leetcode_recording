"""
3.无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

Date: 2025-11-4
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = 0
        left = 0
        for i in range(len(s)):
            if s[i] in dic:
                left = max(left, dic[s[i]] + 1)
            dic[s[i]] = i
            res = max(res, i - left + 1)
        return res
if __name__ == "__main__":
    sol = Solution()
    s1 = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s1))