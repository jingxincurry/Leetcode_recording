""""
1471.数组中的k个最强值
给你一个整数数组 arr 和一个整数 k 。

设 m 为数组的中位数，只要满足下述两个前提之一，就可以判定 arr[i] 的值比 arr[j] 的值更强：

 |arr[i] - m| > |arr[j] - m|
 |arr[i] - m| == |arr[j] - m|，且 arr[i] > arr[j]
请返回由数组中最强的 k 个值组成的列表。答案可以以 任意顺序 返回。

date: 2025-11-5

"""
from typing import List
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        mid = arr[(n - 1) // 2]
        ans = [0] * k
        left, right = 0, n - 1
        for i in range(k):
            if abs(arr[right] - mid) >= abs(arr[left] - mid):
                ans[i] = arr[right]
                right -= 1
            else:
                ans[i] = arr[left]
                left += 1
        return ans
if __name__ == "__main__":
    sol = Solution()
    arr1 = [1,2,3,4,5]
    k1 = 2
    print(sol.getStrongest(arr1, k1))  # [5,1]

    arr2 = [6,7,11,7,6,8]
    k2 = 5
    print(sol.getStrongest(arr2, k2))  # [11,8,6,6,7]

    arr3 = [6,-3,7,2,11]
    k3 = 3
    print(sol.getStrongest(arr3, k3))  # [11,7,-3]