/*
169. Majority Element

给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

date:2026-04-14
*/
#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<unordered_map>
using namespace std;

int majorityelement(vector<int> nums)
{
    int n = nums.size();
        unordered_map<int, int> mp;
        for(int i = 0; i < n; i++)
        {
            mp[nums[i]]++;
        }
        for(auto& [it, cnt]: mp)
        {

            if(cnt > n / 2){
                return it;
            }
        }
        return -1;
}

int main()
{
    vector<int> nums1 = {3,2,3};
    vector<int> nums2 = {2,2,1,1,1,2,2};
    int ans1 = majorityelement(nums1);
    int ans2 = majorityelement(nums2);
    cout << ans1 << endl;
    cout << ans2 << endl;
}