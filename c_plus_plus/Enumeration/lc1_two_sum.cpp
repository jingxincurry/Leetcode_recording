/*
1.两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
你可以按任意顺序返回答案。
*/

#include<iostream>
#include<stdio.h>
#include<unordered_map>
#include<vector>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target){
    unordered_map<int, int> mp;  //键， 值
    for(int i = 0; i < nums.size(); i++){
        int need = target - nums[i];
        if(mp.count(need)){
            return {mp[need], i};
        }
        mp[nums[i]] = i;
    }
    return {};
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
    vector<int> res = twoSum(nums, target);
    for(int x : res) cout << x << " ";
}