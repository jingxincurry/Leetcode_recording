/*
239.滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 date: 2026-04-14

*/

#include<iostream>
#include<stdio.h>
#include<vector>
#include<string>
#include<unordered_map>
using namespace std;

vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> ans;
        int left = 0, right = 0;
        int maxnum = 0;
        while(right < n)
        {
            
            if(right - left + 1 == k){
                for(int i = left; i <= right; i++){
                    maxnum = max(maxnum,nums[i]);
                }
                right++;
            }else if(right - left + 1 < k){
                right++;
            }
            
            if(right - left + 1 > k){
                ans.push_back(maxnum);
                left++;
                maxnum = 0;
            }
        }
        return ans;
    }

int main()
{
    vector<int> nums = {1,3,-1,-3,5,3,6,7};
    int k = 3;
    vector<int> ans = maxSlidingWindow(nums,k);
    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << " ";
    }
}