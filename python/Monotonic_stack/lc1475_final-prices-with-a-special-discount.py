"""
1475.商品折扣后的最终价格

给你一个数组 prices ，其中 prices[i]是商店里第 1 件商品的价格。
商店里正在进行促销活动，如果你要买第 i件商品，那么你可以得到与 prices[j]相等的折扣，其中 j是满足j>i且 prices[j]<= prices[i] 的 最小下标，如果没有满足条件的 j，你将没有任何折扣。

请你返回一个数组，数组中第 i个元素是折扣后你购买商品 i最终需要支付的价格。

"""
from typing import List
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        right = [0] * n
        st = [0]
        for i in range(n - 1, -1, -1):
            p = prices[i]
            while p < st[-1]:
                st.pop()
            right[i] = p - st[-1]
            st.append(prices[i])
        return right
if __name__ == "__main__":
    sol = Solution()
    prices = [8,4,6,2,3]
    print(sol.finalPrices(prices))  # [4,2,4,2,3]