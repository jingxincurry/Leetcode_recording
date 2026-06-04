/*
lc136_single-number.cpp
给你一个整数数组 nums ，除某个元素只出现一次以外，其余每个元素都恰出现两次。请你找出并返回那个只出现了一次的元素。
示例 1：
输入：nums = [2,2,1]
输出：1
示例 2：nums = [4,1,2,1,2]
输出：4
*/
#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

int singlenumber(vector<int> nums){
    int n = nums.size();
    int ans = 0;
    for(int i = 0; i < n; i++){
        ans ^= nums[i];
    }
    return ans;
}

int main()
{
    vector<int> nums1 = {2,2,1};
    int ans = singlenumber(nums1);
    cout << ans << "";
}