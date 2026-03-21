"""
345. 反转字符串中的元音字母

给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。
元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现不止一次。

Date: 2025-11-5

知识点
vol = set("aeiouAEIOU") 设置查询元音
字符串不能修改，转换为列表操作后再转回字符串
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vol = set("aeiouAEIOU")
        s = list(s)
        left,right = 0, len(s) - 1
        while left < right:
            if s[left] in vol and s[right] in vol:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
            elif s[left] in vol:
                right -= 1
            elif s[right] in vol:
                left += 1
            else:
                left += 1
                right -= 1
        return ''.join(s)
    
if __name__ == "__main__":
    sol = Solution()
    s = "IceCreAm"
    print(sol.reverseVowels(s))  # "AmECreIc"