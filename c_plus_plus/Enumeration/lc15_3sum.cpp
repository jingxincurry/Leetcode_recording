/*
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

date:2026-04-03

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include<unordered_map>
#include <algorithm>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums)
{
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> res;
    for(int k = 0; k < n; k++){
        int i = k + 1, j = n - 1;
        if(nums[k] > 0){
                break;
        }
        if(k > 0 && nums[k] == nums[k-1]){
            continue;
        }
        while(i < j){
            int sum = nums[k] + nums[i] + nums[j];
            
            
            if(sum == 0){
                res.push_back({nums[k], nums[i], nums[j]});
                while(i < j && nums[i] == nums[i + 1]) i++;
                while(i < j && nums[j] == nums[j - 1]) j--;
                i++;
                j--;
            }else if(sum < 0){
                i++;
            }else{
                j--;
            }
        }
    }
    return res;
}

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);
    for(int i = 0; i < n; i++){
        cin >> nums[i];
    }
    vector<vector<int>> res = threeSum(nums);
    for(auto &group: res){
        for(int x : group){
            cout << x << " ";
        }
        cout << endl;
    }
    return 0;
}