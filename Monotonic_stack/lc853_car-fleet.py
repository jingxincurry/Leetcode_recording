"""
853.车队

在一条单行道上，有 n 辆车开往同一目的地。目的地是几英里以外的 target 。
给定两个整数数组 position 和 speed ，长度都是 n ，其中 position[i] 是第 i 辆车的位置， speed[i] 是第 i 辆车的速度(单位是英里/小时)。
一辆车永远不会超过前面的另一辆车，但它可以追上去，并以较慢车的速度在另一辆车旁边行驶。
车队 是指并排行驶的一辆或几辆汽车。车队的速度是车队中 最慢 的车的速度。
即便一辆车在 target 才赶上了一个车队，它们仍然会被视作是同一个车队。
返回到达目的地的车队数量 。

data: 2025-11-26
"""
from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = 0
        n = len(position)
        time = [0] * n
        for i, (pos, sp) in enumerate(sorted(zip(position, speed))):
            time[i] = (target - pos) / sp
        
        st = []
        for t in time:
            while st and t >= st[-1]:
                st.pop()
            st.append(t)
        return len(st)
    
if __name__ == "__main__":
    sol = Solution()
    target = 12
    position = [10, 8, 0 ,5, 3]
    speed = [2, 4, 1, 1, 3]
    print(sol.carFleet(target, position, speed))  # 输出[1,1,4,2,1,1,0,0]
    