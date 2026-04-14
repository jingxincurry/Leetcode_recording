/*
3020.子集中元素的最大数量

给你一个 正整数 数组 nums 。
你需要从数组中选出一个满足下述条件的子集：
你可以将选中的元素放置在一个下标从 0 开始的数组中，并使其遵循以下模式：[x, x2, x4, ..., xk/2, xk, xk/2, ..., x4, x2, x]（注意，k 可以是任何 非负 的 2 的幂）。例如，[2, 4, 16, 4, 2] 和 [3, 9, 3] 都符合这一模式，而 [2, 4, 8, 4, 2] 则不符合。
返回满足这些条件的子集中，元素数量的 最大值 。

示例 1：
输入：nums = [5,4,1,2,2]
输出：3
解释：选择子集 {4,2,2} ，将其放在数组 [2,4,2] 中，它遵循该模式，且 22 == 4 。因此答案是 3 。

date: 2026-04-07
*/
#include<iostream>
#include<unordered_map>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int maximumLength(vector<int>& nums) {
        unordered_map<double, int> mp;
        for(int x: nums){
            mp[x]++;
        }
        int maximum = 1;
        
        for(auto& [x, cnt]: mp){
            if(x == 1){
                maximum = max(maximum, cnt - (cnt % 2 ==0));
                continue;
            }
            int len = 1;
            double y = sqrt(x);
            while(mp.count(y) && mp[y]>=2){
                len += 2;
                y = sqrt(y);
            }       
            maximum = max(maximum, len);
        }
        return maximum;
}

int main(){
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    int ans = maximumLength(nums);
    cout << ans << endl;
}