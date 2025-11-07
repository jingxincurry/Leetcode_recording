"""

需求	写法	如果不存在
≥x 的第一个元素的下标	lowerBound(nums,x)	结果为 n
>x 的第一个元素的下标	lowerBound(nums,x+1)	结果为 n
<x 的最后一个元素的下标	lowerBound(nums,x)−1	结果为 −1
≤x 的最后一个元素的下标	lowerBound(nums,x+1)−1	结果为 −1


需求	写法
<x 的元素个数	lowerBound(nums,x)
≤x 的元素个数	lowerBound(nums,x+1)
≥x 的元素个数	n−lowerBound(nums,x)
>x 的元素个数	n−lowerBound(nums,x+1)


"""
from typing import List
def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1 
            else:
                right = mid - 1
        return left