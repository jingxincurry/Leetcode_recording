"""
744.寻找比目标字母大的最小字母

给你一个字符数组 letters，该数组按非递减顺序排序，以及一个字符 target。letters 里至少有两个不同的字符。

返回 letters 中大于 target 的最小的字符。如果不存在这样的字符，则返回 letters 的第一个字符。

"""
from typing import List
class Solution:
    def lower_bound(self, letters:List[str], target: str) ->str:
        left, right = 0, len(letters) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if letters[mid] < target:
                left += 1
            else:
                right -= 1
        return left

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        index = self.lower_bound(letters, chr(ord(target) + 1))
        return letters[index % n]
    
if __name__ == "__main__":
    sol = Solution()
    letters = ["c","f","j"]
    target = "a"
    print(sol.nextGreatestLetter(letters, target))  # "c"