/*
80.删除有序数组中的重复项II
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

date: 2026-04-14
*/

#include<vector>
#include<stdio.h>
#include<iostream>
using namespace std;


int removeDuplicates(vector<int>& nums) {
    int n = nums.size();
    int k = 2;
    for(int i = 2; i < n; i ++){
        if(nums[i] != nums[k - 2]){
            nums[k] = nums[i];
            k++;
        }
    }
    return k;
}

int main()
{
    vector<int> nums1 = {1,1,1,2,2,3};
    int ans = removeDuplicates(nums1);
    cout << ans << endl;
    
}