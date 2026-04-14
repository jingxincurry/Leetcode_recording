/*
11.盛最多的水

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

date: 2026-04-09
*/
#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

int maxWater(vector<int>& nums)
{
    int n = nums.size();
    int maxw = 0;
    int left = 0, right = n - 1;
    while(left < right){
        int s = min(nums[right], nums[left]) * (right - left);
        if( nums[left] < nums[right]){
            maxw = max(maxw, s);
            left++;
        }else{
            maxw = max(maxw, s);
            right--;
        }
    }
    return maxw;
}

int main()
{
    vector<int> nums = {1,8,6,2,5,4,8,3,7};

    cout << maxWater(nums);
}