/*
560.和为K的子数组

给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。
date: 2026-04-14
*/

#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;

int subarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    unordered_map<int, int> mp;
    mp[0]++;
    int cnt = 0;
    int sum = 0;
    for(int i = 0; i < n; i++){
        
        sum += nums[i];
        if(mp.count(sum - k)){
            cnt += mp[sum - k];
        }
        mp[sum]++;
    }
    return cnt;

}

int main()
{
    vector<int> nums = {1,1,1};
    int k = 0;
    int ans = subarraySum(nums, k);
    cout << k << endl;
}