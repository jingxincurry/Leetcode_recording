/*
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个在 不同下标位置 的整数，使它们的和与 target 最接近。

返回这三个数的和。
假定每组输入只存在恰好一个解。

输入：nums = [-1,2,1,-4], target = 1
输出：2

data:2026-04-03
*/
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<unordered_map>
#include<vector>
using namespace std;

int threesum_closest(vector<int>nums, int target)
{
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int clost = INT_MAX;
    for(int i = 0; i < n - 2; i++){
        int left = i + 1, right = n - 1;
        while(left < right){
            int sum = nums[i] + nums[left] + nums[right];
            if(abs(sum - target) < abs(clost - target)){
                clost = sum;
                
            }
            if(sum < target){
                left++;
            }else if(sum - target){
                right--;
            }else{
                return sum;
            }
        }
    }
    return clost;
} 

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    int target;
    cin >> target;
    int ans = threesum_closest(nums, target);
    cout << ans << endl;
    
}