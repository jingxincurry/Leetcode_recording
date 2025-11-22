"""
496.下一个更大元素 I

nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。

给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。

data: 2025-11-21
"""
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx = {x: i for i, x in enumerate(nums1)}  # idx[4] = 0, idx[1] = 1, idx[2] = 2
        ans = [-1] * len(nums1)
        st = []
        for i in range(len(nums2) - 1, -1, -1):
            c = nums2[i]
            while st and c >= st[-1]:
                st.pop()
            if st and c in idx:
                ans[idx[c]] = st[-1]
            st.append(nums2[i])
        return ans
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(sol.nextGreaterElement(nums1, nums2))  # [-1,3,-1]