/*
53.最大子数组和
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。

date:2026-04-14
*/
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;

int maxSubArray(vector<int> nums)
{
    int n = nums.size();
        vector<int> dp(n);
        dp[0] = nums[0];
        for(int i = 1; i < n; i++){
            dp[i] = max(dp[i-1]+ nums[i], nums[i]);
        }
    return *max_element(dp.begin(), dp.end());
}

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }
    int ans = maxSubArray(nums);
    cout << ans << endl;
}